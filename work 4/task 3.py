import json

with open("Book.json", encoding="utf-8") as f:
    data = json.load(f)

for item in data:
    item["DoThis"] = "Козлов Никита Романович"

with open("updated_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)