import re

txt = "Sam1uel10 samuel20 sAM2000m"

print(re.findall("\d{2}|SAM", txt, flags=re.I))

input()
