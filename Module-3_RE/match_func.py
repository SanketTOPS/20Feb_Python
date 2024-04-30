import re

mystr="This is python!"

x=re.match("p",mystr)
print(x)

if x:
    print("Match Done!")
else:
    print("Error!")