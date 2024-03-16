data=[]

n=int(input("Enter number of students:"))

for i in range(n):
    name=input("Enter your name:")
    data.append(name)

x=1
for i in range(n):
    print(f"Student-{x} : {data[i]}")
    x+=1