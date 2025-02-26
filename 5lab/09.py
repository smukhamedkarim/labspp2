
import re

txt="AstanaIsOurCapital"
print(re.sub(r'([a-z])([A-Z])', r'\1 \2', txt))  