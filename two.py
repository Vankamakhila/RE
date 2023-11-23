import re
matcher = re.finditer("a{3}", "ababaabaaaaba")
#                              012345678910

for match in matcher:
    print(match.start(), '....', match.group())