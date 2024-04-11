fl=open('temp.txt','r+')

print(fl.read())
#print(fl.readline())
#print(fl.readlines())
#print(fl.readlines()[3])

"""for i in fl:
    print(i)"""

"""if fl.readable():
    print("Yes...")
else:
    print("Noo")"""


# file write
fl.write("\nHello Students")