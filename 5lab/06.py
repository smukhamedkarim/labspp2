import re
txt = "Hello, world. This is a test"
result = re.sub(r'[ ,.]', ':', txt)
print(result)