import re

mystr="This is Python!216543564654541"

#x=re.findall('^This',mystr)
#x=re.findall('^[A-Z]',mystr)
#x=re.findall('on!$',mystr)
x=re.findall('81$',mystr)
print(x)