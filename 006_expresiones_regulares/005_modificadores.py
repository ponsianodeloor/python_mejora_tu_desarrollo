import re

#el IGNORECASE es un modificador
regex = re.compile(r"ab", re.IGNORECASE)
print (regex.search("PonsianoDeLoorAbSizalema"))