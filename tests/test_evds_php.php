<?php
declare(strict_types=1);

require_once dirname(__DIR__) . '/scripts/fetch_evds_data.php';

$checks = 0;
function check(bool $condition, string $message): void
{
    global $checks;
    $checks++;
    if (!$condition) {
        throw new RuntimeException('TEST FAILED: ' . $message);
    }
}
function rejects(callable $call, string $message): void
{
    $threw = false;
    try {
        $call();
    } catch (RuntimeException $error) {
        $threw = true;
    }
    check($threw, $message);
}
function near(?float $actual, float $expected, string $message): void
{
    check($actual !== null && abs($actual - $expected) < 0.000001, $message);
}

check(evdsDate('2010-1', 'monthly') === '2010-01-31', 'unpadded year-month date');
check(evdsDate('02-2012', 'monthly') === '2012-02-29', 'leap-year month end');
check(evdsDate('04.01.2010', 'daily') === '2010-01-04', 'Turkish daily date');
check(evdsDate('2010-01-04', 'daily') === '2010-01-04', 'ISO daily date');
rejects(fn() => evdsDate('31-02-2010', 'monthly'), 'invalid dates cannot roll forward');

$parsed = evdsParse(['items' => [
    ['Tarih' => '2010-01', 'TP_TEST' => '-12.5'],
    ['Tarih' => '2010-02', 'TP_TEST' => '0'],
    ['Tarih' => '2010-03', 'TP_TEST' => null],
    ['Tarih' => '2010-04', 'TP_TEST' => ''],
    ['Tarih' => '2010-05', 'TP_TEST' => '-1,25'],
]], 'TP.TEST', 'monthly');
near($parsed['2010-01-31']['value'], -12.5, 'negative observations retain their sign');
near($parsed['2010-02-28']['value'], 0.0, 'explicit zero is not missing');
check($parsed['2010-03-31']['value'] === null, 'null remains missing');
check($parsed['2010-04-30']['value'] === null, 'blank remains missing');
near($parsed['2010-05-31']['value'], -1.25, 'decimal comma parsing');

rejects(fn() => evdsParse(['items' => [
    ['Tarih' => '2010-01', 'TP_TEST' => '100'],
    ['Tarih' => '01-01-2010', 'TP_TEST' => '101'],
]], 'TP.TEST', 'monthly'), 'same month in different date formats is duplicate');
rejects(fn() => evdsParse(['items' => array_fill(0, 1000, ['Tarih' => '2010-01', 'TP_TEST' => '100'])],
    'TP.TEST', 'monthly'), 'official 1000-record truncation boundary is rejected');
rejects(fn() => evdsParse(['items' => [['Tarih' => '2010-01', 'WRONG_SERIES' => 100]]],
    'TP.TEST', 'monthly'), 'unrequested series is rejected');

$yoy = evdsYoy([
    ['period_end' => '2009-01-31', 'value' => 100.0, 'source_url' => 'prior-year'],
    ['period_end' => '2009-03-31', 'value' => 200.0, 'source_url' => 'prior-year'],
    ['period_end' => '2010-01-31', 'value' => 110.0, 'source_url' => 'current-year'],
    ['period_end' => '2010-02-28', 'value' => 130.0, 'source_url' => 'current-year'],
    ['period_end' => '2010-03-31', 'value' => 240.0, 'source_url' => 'current-year'],
]);
near($yoy['2010-01-31']['value'], 10.0, 'January year-on-year change');
near($yoy['2010-03-31']['value'], 20.0, 'March uses March, not compressed row positions');
check($yoy['2010-02-28']['value'] === null, 'missing previous February is not filled');
check($yoy['2010-01-31']['source_url'] === 'current-year', 'numerator provenance is preserved');
check($yoy['2010-01-31']['denominator_source_url'] === 'prior-year', 'denominator provenance is preserved');
rejects(fn() => evdsYoy([
    ['period_end' => '2009-01-01', 'value' => 100.0],
    ['period_end' => '2009-01-31', 'value' => 101.0],
]), 'duplicate calendar month cannot enter annual change');
$zeroBase = evdsYoy([
    ['period_end' => '2009-01-31', 'value' => 0.0],
    ['period_end' => '2010-01-31', 'value' => 100.0],
]);
check($zeroBase['2010-01-31']['value'] === null, 'zero denominator is not an infinite observation');

evdsValidateUrl(EVDS_BASE . 'series=TP.TEST&type=json');
check(true, 'official HTTPS URL accepted');
foreach ([
    'https://evds3.tcmb.gov.tr.attacker.example/igmevdsms-dis/',
    'https://attacker.example/igmevdsms-dis/',
    'http://evds3.tcmb.gov.tr/igmevdsms-dis/',
    'https://user:password@evds3.tcmb.gov.tr/igmevdsms-dis/',
    'https://evds3.tcmb.gov.tr:8443/igmevdsms-dis/',
] as $invalidUrl) {
    rejects(fn() => evdsValidateUrl($invalidUrl), 'credential destination is pinned');
}

$csv = evdsCsv([
    ['series_name' => 'Seri, "alıntı"', 'value' => -1.25, 'missing' => null],
    ['series_name' => "İkinci\nsatır", 'value' => 0.0, 'denominator_source_url' => 'prior-year'],
]);
check(str_starts_with($csv, "\xEF\xBB\xBF"), 'CSV UTF-8 BOM');
$stream = fopen('php://temp', 'r+');
fwrite($stream, substr($csv, 3));
rewind($stream);
$header = fgetcsv($stream, null, ',', '"', '');
$first = array_combine($header, fgetcsv($stream, null, ',', '"', ''));
$second = array_combine($header, fgetcsv($stream, null, ',', '"', ''));
fclose($stream);
check($first['series_name'] === 'Seri, "alıntı"', 'CSV comma and quote round trip');
near((float) $first['value'], -1.25, 'CSV negative number round trip');
check($first['missing'] === '', 'CSV null is blank');
check($second['series_name'] === "İkinci\nsatır", 'CSV embedded newline round trip');
near((float) $second['value'], 0.0, 'CSV explicit zero remains zero');
check($second['denominator_source_url'] === 'prior-year', 'CSV union retains denominator columns');

$boundary = evdsParse(['items' => [
    ['Tarih' => '31-12-2010', 'TP_TEST' => 10],
    ['Tarih' => '07-01-2011', 'TP_TEST' => 11],
]], 'TP.TEST', 'weekly');
$currentYear = evdsCropBatch($boundary, 2011, 'weekly');
check(count($currentYear) === 1, 'preceding Friday does not duplicate the prior year');
near($currentYear['2011-01-07']['value'], 11, 'requested-year weekly observation is retained');
rejects(fn() => evdsCropBatch($boundary, 2011, 'daily'), 'daily batches cannot borrow a prior-year observation');
rejects(fn() => evdsCropBatch(evdsParse(['items' => [
    ['Tarih' => '01-10-2010', 'TP_TEST' => 10],
    ['Tarih' => '07-01-2011', 'TP_TEST' => 11],
]], 'TP.TEST', 'weekly'), 2011, 'weekly'), 'unexpected distant weekly date rejected');

echo "PASS: $checks independent PHP checks\n";
