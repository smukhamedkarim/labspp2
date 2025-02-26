import re
txt = "ab aXb a123b axxb aac acb"
matches = re.findall(r'a.*b', txt)
print(matches)