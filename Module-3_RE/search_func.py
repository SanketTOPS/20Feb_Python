import re

mystr="This is python!"

x=re.search("python",mystr)
print(x)

if x:
    print("Match Done!")
else:
    print("Error!")