<?php
declare(strict_types=1);

// TCMB EVDS3: API key only in the HTTP header. Run with --help.
const EVDS_BASE = 'https://evds3.tcmb.gov.tr/igmevdsms-dis/';

function evdsValidateUrl(string $url): void
{
    $p = parse_url($url);
    if (!$p || ($p['scheme'] ?? '') !== 'https' || ($p['host'] ?? '') !== 'evds3.tcmb.gov.tr'
        || !str_starts_with($p['path'] ?? '', '/igmevdsms-dis/')
        || isset($p['user']) || isset($p['pass']) || (isset($p['port']) && $p['port'] !== 443)) {
        throw new RuntimeException('Anahtar yalnız resmi TCMB HTTPS adresine gönderilebilir.');
    }
}

function evdsRequest(string $url, string $key): array
{
    evdsValidateUrl($url);
    if (!extension_loaded('curl')) {
        throw new RuntimeException('PHP cURL eklentisi gerekli.');
    }
    for ($attempt = 0; $attempt < 3; $attempt++) {
        $ch = curl_init($url);
        curl_setopt_array($ch, [
            CURLOPT_HTTPHEADER => ['key: ' . $key, 'Accept: application/json'],
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_FOLLOWLOCATION => false,
            CURLOPT_CONNECTTIMEOUT => 10,
            CURLOPT_TIMEOUT => 30,
            CURLOPT_SSL_VERIFYPEER => true,
            CURLOPT_SSL_VERIFYHOST => 2,
            CURLOPT_USERAGENT => 'BilancoResearch-PHP/1.0',
        ]);
        $raw = curl_exec($ch);
        $http = (int) curl_getinfo($ch, CURLINFO_HTTP_CODE);
        $error = curl_errno($ch);
        // PHP 8 CurlHandle closes when released; curl_close is deprecated in 8.5.
        unset($ch);
        if ($http === 401 || $http === 403) {
            throw new RuntimeException("EVDS anahtarı kabul edilmedi (HTTP $http). Anahtar kayda yazılmadı.");
        }
        if ($http >= 300 && $http < 400) {
            throw new RuntimeException('Yönlendirme reddedildi; anahtar başka adrese iletilmedi.');
        }
        if (($http === 429 || $error !== 0 || $http >= 500) && $attempt < 2) {
            sleep(2 * ($attempt + 1));
            continue;
        }
        if ($raw === false || $error !== 0 || $http !== 200) {
            throw new RuntimeException("EVDS bağlantısı başarısız (HTTP $http, cURL $error).");
        }
        try {
            $payload = json_decode($raw, true, 512, JSON_THROW_ON_ERROR);
        } catch (JsonException $e) {
            throw new RuntimeException('EVDS geçerli JSON döndürmedi. Yanıt veri dosyası sayılmadı.');
        }
        return [$raw, $payload];
    }
    throw new RuntimeException('EVDS üç denemede yanıt vermedi.');
}

function evdsDate(string $raw, string $frequency): string
{
    $raw = trim($raw);
    if (preg_match('/^(\d{4})-(\d{1,2})$/', $raw, $m)) {
        [$year, $month, $day] = [(int) $m[1], (int) $m[2], 1];
    } elseif (preg_match('/^(\d{1,2})-(\d{4})$/', $raw, $m)) {
        [$year, $month, $day] = [(int) $m[2], (int) $m[1], 1];
    } elseif (preg_match('/^(\d{1,2})[-.](\d{1,2})[-.](\d{4})$/', $raw, $m)) {
        [$year, $month, $day] = [(int) $m[3], (int) $m[2], (int) $m[1]];
    } elseif (preg_match('/^(\d{4})-(\d{2})-(\d{2})$/', $raw, $m)) {
        [$year, $month, $day] = [(int) $m[1], (int) $m[2], (int) $m[3]];
    } else {
        throw new RuntimeException('EVDS tarih biçimi tanınmadı.');
    }
    if (!checkdate($month, $day, $year)) {
        throw new RuntimeException('EVDS geçersiz gözlem tarihi döndürdü.');
    }
    $date = new DateTimeImmutable(sprintf('%04d-%02d-%02d', $year, $month, $day));
    return ($frequency === 'monthly' ? $date->modify('last day of this month') : $date)->format('Y-m-d');
}

function evdsParse(array $payload, string $code, string $frequency): array
{
    $items = $payload['items'] ?? null;
    if (!is_array($items) || count($items) === 0) {
        throw new RuntimeException('EVDS gözlem listesi boş veya beklenen biçimde değil.');
    }
    if (count($items) >= 1000) {
        throw new RuntimeException('1000 gözlem sınırına ulaşıldı; tarih aralığı küçültülmeli.');
    }
    $rows = [];
    foreach ($items as $item) {
        $field = str_replace('.', '_', $code);
        if (!array_key_exists($field, $item)) {
            $field = $code;
        }
        if (!isset($item['Tarih']) || !array_key_exists($field, $item)) {
            throw new RuntimeException('Yanıtta istenen tarih veya seri alanı yok.');
        }
        $date = evdsDate((string) $item['Tarih'], $frequency);
        if (array_key_exists($date, $rows)) {
            throw new RuntimeException('Aynı dönem için yinelenen EVDS gözlemi.');
        }
        $raw = $item[$field];
        $text = trim((string) ($raw ?? ''));
        if ($raw === null || in_array($text, ['', '-', 'NA', 'N/A', 'NaN', 'null'], true)) {
            $value = null;
        } else {
            $text = str_replace(',', '.', $text);
            if (!is_numeric($text)) {
                throw new RuntimeException('EVDS sayısal alanında tanınmayan değer.');
            }
            $value = (float) $text;
            if (!is_finite($value)) {
                $value = null;
            }
        }
        $rows[$date] = ['period_end' => $date, 'value' => $value];
    }
    ksort($rows);
    return $rows;
}

function evdsYoy(array $rows): array
{
    $byMonth = [];
    foreach ($rows as $row) {
        $month = substr($row['period_end'], 0, 7);
        if (array_key_exists($month, $byMonth)) {
            throw new RuntimeException('Yıllık değişimde bir ayda birden fazla gözlem olamaz.');
        }
        $byMonth[$month] = $row;
    }
    $out = [];
    foreach ($rows as $row) {
        $year = (int) substr($row['period_end'], 0, 4);
        $previousMonth = ($year - 1) . substr($row['period_end'], 4, 3);
        $previous = $byMonth[$previousMonth] ?? null;
        $value = $row['value'];
        $row['value'] = $value !== null && $previous !== null && $previous['value'] !== null && $previous['value'] > 0
            ? 100 * ($value / $previous['value'] - 1) : null;
        foreach (['source_url', 'source_sha256', 'retrieved_at', 'vintage_id'] as $field) {
            $row['denominator_' . $field] = $previous[$field] ?? '';
        }
        $row['transformation'] = '100*(index_this_month/index_same_month_last_year-1)';
        $out[$row['period_end']] = $row;
    }
    return $out;
}

function evdsCropBatch(array $rows, int $year, string $frequency): array
{
    $retained = [];
    foreach ($rows as $date => $row) {
        if (substr($date, 0, 4) === (string) $year) {
            $retained[$date] = $row;
            continue;
        }
        // EVDS weekly requests may include the preceding Friday at January 1.
        // Keep the raw response, but assign observations by their actual date.
        $stamp = new DateTimeImmutable($date);
        if ($frequency !== 'weekly' || $stamp < new DateTimeImmutable("$year-01-01 -7 days")
            || $stamp > new DateTimeImmutable("$year-12-31 +7 days")) {
            throw new RuntimeException('Beklenmeyen dönem dışı EVDS gözlemi.');
        }
    }
    if ($retained === []) {
        throw new RuntimeException('İstenen yıl içinde EVDS gözlemi bulunamadı.');
    }
    return $retained;
}

function evdsWrite(string $path, string $bytes): void
{
    if (!is_dir(dirname($path)) && !mkdir(dirname($path), 0775, true) && !is_dir(dirname($path))) {
        throw new RuntimeException('Çıktı klasörü oluşturulamadı.');
    }
    if (file_put_contents($path . '.tmp', $bytes) === false || !rename($path . '.tmp', $path)) {
        throw new RuntimeException('Çıktı dosyası kaydedilemedi.');
    }
}

function evdsCsv(array $rows): string
{
    $fields = [];
    foreach ($rows as $row) {
        foreach (array_keys($row) as $key) {
            $fields[$key] = true;
        }
    }
    $fields = array_keys($fields);
    $stream = fopen('php://temp', 'r+');
    fwrite($stream, "\xEF\xBB\xBF");
    fputcsv($stream, $fields, ',', '"', '');
    foreach ($rows as $row) {
        fputcsv($stream, array_map(static fn($f) => $row[$f] ?? '', $fields), ',', '"', '');
    }
    rewind($stream);
    $csv = stream_get_contents($stream);
    fclose($stream);
    return $csv;
}

function evdsDownload(array $spec, string $key, string $directory, int $first = 2010, int $last = 2020): array
{
    $observations = [];
    $receipts = [];
    $coverage = [];
    foreach ($spec as $series) {
        $code = $series['series_code'] ?? '';
        if (!preg_match('/^[A-Z0-9.]+$/D', $code) || empty($series['definition_verified']) || empty($series['metadata_url'])) {
            throw new RuntimeException('Yalnız resmî tanımı doğrulanmış seriler kullanılabilir.');
        }
        $yoy = ($series['transformation'] ?? 'level') === 'year_on_year_percent';
        $rows = [];
        // Annual batches keep every request below the official 1000-observation limit.
        for ($year = $yoy ? $first - 1 : $first; $year <= $last; $year++) {
            $url = EVDS_BASE . "series=$code&startDate=01-01-$year&endDate=31-12-$year&type=json&formulas=0";
            $path = $directory . '/raw/' . str_replace('.', '_', $code) . "_$year.json";
            $receiptPath = substr($path, 0, -5) . '.receipt.json';
            $cached = false;
            if (is_file($path) && is_file($receiptPath)) {
                $oldReceipt = json_decode(file_get_contents($receiptPath), true, 512, JSON_THROW_ON_ERROR);
                $cached = ($oldReceipt['source_url'] ?? '') === $url
                    && ($oldReceipt['sha256'] ?? '') === hash_file('sha256', $path);
            }
            if ($cached) {
                $raw = file_get_contents($path);
                $payload = json_decode($raw, true, 512, JSON_THROW_ON_ERROR);
            } else {
                [$raw, $payload] = evdsRequest($url, $key);
            }
            $parsed = evdsParse($payload, $code, $series['frequency']);
            $part = evdsCropBatch($parsed, $year, $series['frequency']);
            $receipt = ['source_url' => $url, 'series_code' => $code, 'feature_id' => $series['feature_id'],
                'metadata_url' => $series['metadata_url'], 'requested_year' => $year, 'rows' => count($part),
                'raw_rows' => count($parsed), 'excluded_boundary_rows' => count($parsed) - count($part),
                'retrieved_at' => $cached ? $oldReceipt['retrieved_at'] : gmdate('c'), 'sha256' => hash('sha256', $raw),
                'retrieval_mode' => $cached ? 'verified_cache' : 'fresh_http',
                'source_vintage_status' => 'latest_snapshot_original_publication_unverified'];
            foreach ($part as $date => &$row) {
                if (substr($date, 0, 4) !== (string) $year || isset($rows[$date])) {
                    throw new RuntimeException('Dönem dışı veya yinelenen EVDS kaydı.');
                }
                $row += ['feature_id' => $series['feature_id'], 'series_name' => $series['series_name'],
                    'unit' => $series['unit'], 'series_code' => $code, 'base_period' => $series['base_period'] ?? '',
                    'source_url' => $url, 'source_sha256' => $receipt['sha256'], 'retrieved_at' => $receipt['retrieved_at'],
                    'metadata_url' => $series['metadata_url'], 'vintage_id' => substr($receipt['sha256'], 0, 16),
                    'publication_date' => '', 'available_at' => '', 'pit_eligible' => 'False',
                    'availability_status' => 'historical_release_and_vintage_unverified',
                    'source_fetch_status' => 'downloaded', 'source_provenance_status' => 'downloaded_from_source',
                    'release_rule' => 'Latest EVDS vintage; observation date is not original publication date'];
            }
            unset($row);
            $rows += $part;
            evdsWrite($path, $raw);
            evdsWrite($receiptPath, json_encode($receipt, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_THROW_ON_ERROR));
            $receipts[] = $receipt;
            echo "$code $year: " . count($part) . " gözlem\n";
            usleep(300000);
        }
        ksort($rows);
        $views = [];
        if ($yoy) {
            $levels = $rows;
            foreach ($levels as &$level) {
                $level['series_name'] .= '_index_level';
                $level['unit'] = $series['raw_unit'] ?? 'index';
            }
            unset($level);
            $views[] = $levels;
            $views[] = evdsYoy($rows);
        } else {
            $views[] = $rows;
        }
        foreach ($views as $view) {
            $numeric = 0;
            foreach ($view as $date => $row) {
                if (substr($date, 0, 4) >= (string) $first) {
                    $observations[] = $row;
                    $numeric += $row['value'] !== null ? 1 : 0;
                }
            }
            if ($numeric === 0) {
                throw new RuntimeException('İstenen serilerden birinde sayısal veri yok; eksik sonuç yayımlanmadı.');
            }
            for ($year = $first; $year <= $last; $year++) {
                $part = array_filter($view, static fn($r) => substr($r['period_end'], 0, 4) === (string) $year);
                $months = [];
                $count = 0;
                foreach ($part as $row) {
                    if ($row['value'] !== null) {
                        $count++;
                        $months[(int) substr($row['period_end'], 5, 2)] = true;
                    }
                }
                $missing = $series['frequency'] === 'monthly' ? array_diff(range(1, 12), array_keys($months)) : [];
                $coverage[] = ['series_name' => reset($view)['series_name'], 'series_code' => $code,
                    'feature_id' => $series['feature_id'], 'year' => $year, 'frequency' => $series['frequency'],
                    'rows' => count($part), 'nonmissing' => $count, 'missing_values' => count($part) - $count,
                    'missing_expected_months' => implode('|', $missing),
                    'monthly_grid_complete' => $series['frequency'] === 'monthly' ? (count($missing) === 0 ? 'True' : 'False') : 'not_applicable'];
            }
        }
    }
    evdsWrite($directory . '/observations.csv', evdsCsv($observations));
    evdsWrite($directory . '/series_year_coverage.csv', evdsCsv($coverage));
    $manifest = ['implementation' => 'PHP cURL', 'official_guide' => EVDS_BASE . 'documents/showDocument?docId=8',
        'first_year' => $first, 'last_year' => $last, 'requests' => $receipts, 'rows' => count($observations),
        'numerical_observations' => count(array_filter($observations, static fn($r) => $r['value'] !== null)),
        'historical_pit_eligible' => 0, 'key_logged_or_exported' => false];
    evdsWrite($directory . '/manifest.json', json_encode($manifest, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_THROW_ON_ERROR));
    return $manifest;
}

function evdsMain(): int
{
    $options = getopt('', ['spec:', 'key-file:', 'delete-key-file', 'prompt-key', 'help']);
    if (isset($options['help'])) {
        echo "PHP ile EVDS → CSV\nphp scripts/fetch_evds_data.php --prompt-key\n";
        echo "Alternatif: EVDS_API_KEY ortam değişkeni veya --key-file DOSYA\n";
        echo "Anahtarı koda/sohbete eklemeyin. Çıktı: data/external/rebuilt/evds/\n";
        return 0;
    }
    $keyFile = $options['key-file'] ?? null;
    try {
        $key = $keyFile !== null ? trim((string) file_get_contents($keyFile)) : trim((string) getenv('EVDS_API_KEY'));
        if (isset($options['prompt-key'])) {
            if (!stream_isatty(STDIN)) {
                throw new RuntimeException('Gizli giriş için etkileşimli Terminal penceresi gerekli.');
            }
            $state = trim((string) shell_exec('stty -g'));
            if ($state === '') {
                throw new RuntimeException('Gizli terminal girişi açılamadı.');
            }
            fwrite(STDERR, 'EVDS API anahtarı (yazarken görünmez): ');
            shell_exec('stty -echo');
            try {
                $key = trim((string) fgets(STDIN));
            } finally {
                shell_exec('stty ' . escapeshellarg($state));
                fwrite(STDERR, "\n");
            }
        }
        $root = dirname(__DIR__);
        if ($key === '' && is_file($root . '/.env')) {
            foreach (file($root . '/.env', FILE_IGNORE_NEW_LINES) as $line) {
                if (str_starts_with(trim($line), 'EVDS_API_KEY=')) {
                    $key = trim(substr(trim($line), strlen('EVDS_API_KEY=')), " \"'");
                }
            }
        }
        if ($key === '' || strlen($key) > 512 || preg_match('/\s/', $key)) {
            throw new RuntimeException('EVDS anahtarı girilmedi veya biçimi geçersiz.');
        }
        $spec = json_decode(file_get_contents($options['spec'] ?? $root . '/config/evds_series.json'), true, 512, JSON_THROW_ON_ERROR);
        $manifest = evdsDownload($spec, $key, $root . '/data/external/rebuilt/evds');
        echo 'Tamamlandı: ' . $manifest['rows'] . " kayıt.\n";
        return 0;
    } catch (Throwable $e) {
        fwrite(STDERR, $e->getMessage() . "\n");
        return 1;
    } finally {
        if (isset($options['delete-key-file']) && $keyFile !== null && is_file($keyFile)) {
            unlink($keyFile);
        }
    }
}

if (realpath($_SERVER['SCRIPT_FILENAME'] ?? '') === __FILE__) {
    exit(evdsMain());
}
