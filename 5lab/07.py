import re
txt = "hello_world_this_is_python"
matches = re.sub(r'_([a-z])', lambda x: x.group(1).upper(), txt)
print(matches)