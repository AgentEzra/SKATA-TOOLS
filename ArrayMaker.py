import json

with open("kbbi.txt", "r", encoding="utf-8") as f:
    words = [line.strip().lower() for line in f if line.strip()]

with open("kbbi.json", "w", encoding="utf-8") as f:
    json.dump(words, f, ensure_ascii=False, indent=2)

print(f"Saved {len(words)} words to kbbi.json")
