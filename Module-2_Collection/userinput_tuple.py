data=[]

n=int(input("Enter number of elements:"))

for i in range(n):
    x=input("Enter any value:")
    data.append(x)

print(tuple(data))