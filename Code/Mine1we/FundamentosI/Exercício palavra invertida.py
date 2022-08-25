import re

m = re.findall(r"[^\-,.?!\s]+", "mentiras disseram verdades")[::-1]

print(*m)
