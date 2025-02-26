import re
txt = "ab a abb abbb abbbb abc aab"
matches = re.findall(r'ab{2,3}', txt)
print(matches)