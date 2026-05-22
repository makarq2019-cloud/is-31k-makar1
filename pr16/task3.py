import re

text = "test@example.com"
pattern = r"^[\w.-]+@[\w.-]+\.\w+$"

print(bool(re.match(pattern, text)))