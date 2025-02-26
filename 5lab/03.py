import re
txt = "hello_world this_is a_test not_a_match"
matches = re.findall(r'\b[a-z]+_[a-z]+\b', txt)
print(matches)