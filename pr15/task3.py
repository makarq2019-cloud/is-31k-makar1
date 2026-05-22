import string

with open("input.txt", encoding="utf-8") as f:
    text = f.read()

clean = text.translate(str.maketrans('', '', string.punctuation))

with open("clean.txt", "w", encoding="utf-8") as f:
    f.write(clean)

print("Saved to clean.txt")