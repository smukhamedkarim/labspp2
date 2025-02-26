import re
txt = "Hello world This is A Test Abc XYZ abcDef"
matches = re.findall(r'\b[A-Z][a-z]+\b', txt)
print(matches)