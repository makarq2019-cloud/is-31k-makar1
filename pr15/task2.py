from collections import Counter

with open("input.txt", encoding="utf-8") as f:
    words = f.read().lower().split()

counts = Counter(words)

for word, count in counts.most_common():
    print(word, count)