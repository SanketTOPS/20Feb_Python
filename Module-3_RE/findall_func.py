import re

mystr="This is python!"

x=re.findall('is',mystr)
print(x)

if x:
    print("Match Done!")
else:
    print("Error!")