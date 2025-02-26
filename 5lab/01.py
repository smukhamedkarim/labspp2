import re

txt = "ab a abb abbb ac abc aab"
matches = re.findall(r'ab*', txt)
print(matches)