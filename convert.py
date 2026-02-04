import csv
import json

cafes = []
with open("ร้านคาเฟ่.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter="\t")
    for i, row in enumerate(reader, start=1):
        cafes.append({
            "ชื่อร้าน": row["ชื่อร้าน"],
            "ที่อยู่": row["ที่อยู่"],
            "เวลา เปิด-ปิด": row["เวลา เปิด-ปิด"],
            "เบอร์โทร": row["เบอร์โทร"],
            "ภาพ": f"images/cafe{i}.jpg"  # เพิ่มช่องภาพอัตโนมัติ
        })

with open("cafes.json", "w", encoding="utf-8") as f:
    json.dump(cafes, f, ensure_ascii=False, indent=2)

print("✅ สร้างไฟล์ cafes.json เรียบร้อยแล้ว")