#!/usr/bin/env python3
"""Validate the living feature registry and render its Turkish review document."""

import argparse
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "docs/model_oncesi/degiskenler.json"
OUTPUT = ROOT / "docs/model_oncesi/DEGISKEN_LISTESI.md"


def validate(data):
    features = data["features"]
    ids = [row["id"] for row in features]
    if len(ids) != len(set(ids)):
        raise ValueError("Değişken kimlikleri benzersiz olmalı")
    known = set(ids)
    target_ids = {row["id"] for row in data["targets"]}
    for row in features:
        if row["priority"] not in data["priorities"]:
            raise ValueError("Geçersiz öncelik: " + row["id"])
        if row["group"] not in data["groups"]:
            raise ValueError("Geçersiz grup: " + row["id"])
        for field, choices in data["status_values"].items():
            if row[field] not in choices:
                raise ValueError("Geçersiz durum: " + row["id"] + "/" + field)
        if row["direction_policy"] != "learn_from_data":
            raise ValueError("Etkinin yönü veriden öğrenilmeli: " + row["id"])
        if not set(row["depends_on"]).issubset(known - {row["id"]}):
            raise ValueError("Geçersiz bağımlılık: " + row["id"])
        if not set(row["source_ids"]).issubset(data["sources"]):
            raise ValueError("Geçersiz kaynak: " + row["id"])
        if not set(row["related_targets"]).issubset(target_ids):
            raise ValueError("Geçersiz hedef: " + row["id"])
    visiting, visited = set(), set()
    by_id = {row["id"]: row for row in features}

    def visit(key):
        if key in visiting:
            raise ValueError("Döngüsel bağımlılık: " + key)
        if key in visited:
            return
        visiting.add(key)
        for dependency in by_id[key]["depends_on"]:
            visit(dependency)
        visiting.remove(key)
        visited.add(key)

    for key in ids:
        visit(key)
    accepted = {row["id"] for row in features if row["selection_status"] == "accepted"}
    if not set(data["confirmed_input_ids"]).issubset(accepted):
        raise ValueError("Kullanıcının seçtiği endeksler kabul edilmiş kalmalı")


def cell(value):
    if isinstance(value, list):
        value = "; ".join(value)
    return str(value).replace("|", "\\|").replace("\n", " ")


def render(data):
    rows = data["features"]
    counts = Counter(row["priority"] for row in rows)
    lines = [
        "# Güncellenebilir değişken listesi",
        "",
        f"Sürüm: **{data['version']}** · Son inceleme: **{data['updated_at']}** · Durum: **taslak, eğitilmiş sonuç yok**.",
        "",
        data["purpose"],
        "",
        "Çalışma alanı: [model öncesi / geliştirme ve eğitim](README.md). Aynı tanım sözlüğü [model sonrası tahmin ve işletimde](../model_sonrasi/README.md) de kullanılır; seçilmiş modelin kesin girdi sürümü ayrıca sabitlenir.",
        "",
        "**Yetkili kayıt:** [degiskenler.json](degiskenler.json). Bu Markdown aynı kayıttan üretilir. Kaynak dosyayı güncelledikten sonra depo kökünde `python3 scripts/render_feature_list.py` çalıştırın; eşleşmeyi denetlemek için `--check` ekleyin. [Üretici betik](../../scripts/render_feature_list.py).",
        "",
        f"Listede **{len(rows)} özellik ailesi** var: **{counts['P0']} P0**, **{counts['P1']} P1**, **{counts['P2']} P2**. Bunlar sütun sayısı değildir: bir aile birden fazla ham kalem, gecikme veya oran içerebilir. İlk deneyde hepsi açılmayacak.",
        "",
        "## Kabul edilen kararlar",
        "",
    ]
    lines += ["- " + note for note in data["confirmed_decisions"]]
    lines += ["", "## Öncelik ve durumlar", ""]
    lines += [f"- **{key}:** {value}" for key, value in data["priorities"].items()]
    lines += [
        "",
        "Seçim, veri hazırlığı ve deney kanıtı ayrı tutulur. `accepted` kullanma kararı; `verified` veri doğrulaması; `locked_test_evaluated` sabit test değerlendirmesidir. Biri diğerini garanti etmez. Şimdilik bütün aileler veri eşleme aşamasındadır ve test edilmemiştir.",
        "",
        "## Şirketlerin aynı olaya farklı tepkisi",
        "",
        data["heterogeneity_note"],
        "",
        "| Ortak olay | Şirket profili | Olası kanallar; beklenen sonuç etiketi değildir |",
        "|---|---|---|",
    ]
    lines += ["| " + " | ".join(cell(row[key]) for key in ("event", "profile", "channels")) + " |" for row in data["event_examples"]]
    lines += ["", "## Özellik aileleri", ""]
    for group, title in data["groups"].items():
        lines += [f"### {title}", "", "| ID / öncelik / karar | Değişken ailesi | İlk temsil | En ilgili hedefler | Kaynak |", "|---|---|---|---|---|"]
        for row in rows:
            if row["group"] != group:
                continue
            refs = ", ".join(f"[{key}]({data['sources'][key]['url']})" for key in row["source_ids"])
            targets = "Bütün hedefler" if len(row["related_targets"]) == len(data["targets"]) else ", ".join(row["related_targets"])
            decision = "seçildi" if row["selection_status"] == "accepted" else "aday" if row["selection_status"] == "candidate" else "reddedildi"
            values = [f"{row['id']} · {row['priority']} · {decision}", row["label"], row["representation"], targets, refs]
            lines.append("| " + " | ".join(cell(value) for value in values) + " |")
        lines += ["", "Tanım ve veri sınırları:", ""]
        for row in rows:
            if row["group"] == group:
                lines.append(f"- **{row['id']}:** {row['definition']} **Sınır:** {row['caveat']}")
        lines.append("")
    lines += ["## Hedef sözlüğü", "", "Bunlar tahmin edilen gelecekteki kalemlerdir; yukarıdaki girdiler bunların geçmiş değerlerini de içerebilir.", "", "| ID | Hedef | Tür |", "|---|---|---|"]
    lines += [f"| {row['id']} | {row['label']} | {row['period_type']} |" for row in data["targets"]]
    lines += ["", "## Zaman ve veri sözleşmesi", ""]
    lines += ["- " + note for note in data["data_contract"]]
    lines += ["", "Her ham gözlemde tutulacak alanlar:", "", "| Alan | Anlamı |", "|---|---|"]
    lines += [f"| `{key}` | {cell(value)} |" for key, value in data["observation_fields"].items()]
    lines += ["", "## Karşılaştırma planı", "", "| Deney | Girdi | Sorduğu soru |", "|---|---|---|"]
    lines += [f"| {row['id']} | {cell(row['inputs'])} | {cell(row['question'])} |" for row in data["experiments"]]
    lines += ["", data["evaluation_note"], "", "## İki haftalık veri pilotu", "", data["pilot"], "", "## Listeyi güncelleme", ""]
    lines += ["- " + note for note in data["maintenance_rules"]]
    lines += ["", "## Beş uzman incelemesinin kapsamı", ""]
    lines += [f"- **{row['area']}:** {row['decision']}" for row in data["review_areas"]]
    lines += ["", "Bu incelemeler model başarısı kanıtı veya beş bağımsız deney değildir; tasarım kontrolüdür.", "", "## Kaynaklar ve kanıt sınırı", ""]
    lines += [f"- **{key}:** [{row['title']}]({row['url']}) — {row['scope']}" for key, row in data["sources"].items()]
    lines += ["", "## Geliştirici deneyimi notları", "", "İki uygulama yazısının tam metni ve yorumları incelendi; ikisinde de yorum bulunmadı. İlki bir veri sağlayıcısının deneyimidir; bu inceleme akademik kanıt veya topluluk uzlaşısı değildir.", ""]
    for row in data.get("community_notes", []):
        lines.append(f"- {row['emoji']} [{row['title']}]({row['url']}) [@{row['username']}](https://dev.to/{row['username']}) — {row['takeaway']} 🔗 [Read Full Discussion on DEV]({row['url']})")
    lines += ["", "## Değişiklik kaydı", ""]
    lines += [f"- **{row['version']} / {row['date']}:** {row['note']}" for row in data["change_log"]]
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Dosyaları değiştirmeden eşleşmeyi denetle")
    args = parser.parse_args()
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    validate(data)
    result = render(data)
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != result:
            parser.exit(1, "Markdown güncel değil; betiği --check olmadan çalıştırın.\n")
    else:
        OUTPUT.parent.mkdir(parents=True, exist_ok=True)
        OUTPUT.write_text(result, encoding="utf-8")
    counts = Counter(row["priority"] for row in data["features"])
    print(f"Doğrulandı: {len(data['features'])} aile; {dict(counts)}; {len(data['targets'])} hedef.")


if __name__ == "__main__":
    main()
