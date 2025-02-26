import re
txt = "SplitAtUppercaseLetters"
matches = re.findall(r'[A-Z][a-z]*', txt)
print(matches)