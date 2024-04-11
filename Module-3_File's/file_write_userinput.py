fl=open('hello.txt','a')


id=input("Enter your ID:")
name=input("Enter your Name:")

"""fl.write(id)
fl.write(name)"""


fl.write(f"ID:{id}")
fl.write(f"\nName:{name}\n")