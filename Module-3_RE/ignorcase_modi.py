import re

mystr="This is Python!456546"

#x=re.findall('[A-Z]',mystr)
#x=re.findall('[a-z]',mystr)
#x=re.findall('[0-9]',mystr)
#x=re.findall('[A-Za-z0-9]',mystr)
x=re.findall('[A-Za-z]',mystr)
print(x)