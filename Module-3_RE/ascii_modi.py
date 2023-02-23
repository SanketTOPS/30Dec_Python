import re

mystr="This is Python!68454"

#x=re.findall('\w',mystr) #word
#x=re.findall('\W',mystr) #non-word
#x=re.findall('\d',mystr) #digit
#x=re.findall('\D',mystr) #non-digit
#x=re.findall('\s',mystr) #space
#x=re.findall('\S',mystr) #non-space
#x=re.findall(r'\bThis',mystr) #starting check
#x=re.findall('\B58',mystr) #ending check
#x=re.findall('\AThis',mystr) #starting check
x=re.findall('54\Z',mystr) #ending check
print(x)