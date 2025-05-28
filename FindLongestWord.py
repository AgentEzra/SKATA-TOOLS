import json

# Load the word list
with open("kbbi.json", "r", encoding="utf-8") as f:
    words = json.load(f)

# Sort words by length, descending
sorted_words = sorted(words, key=len, reverse=True)

# Get top 5 longest (remove duplicates if needed)
top_5 = []
seen = set()
for word in sorted_words:
    if word not in seen:
        top_5.append(word)
        seen.add(word)
    if len(top_5) == 50:
        break

# Print results
for i, word in enumerate(top_5, 1):
    print(f"{i}. {word} ({len(word)} huruf)")
