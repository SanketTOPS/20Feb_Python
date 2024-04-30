n=int(input("Enter any number to check it's perfect or not:"))

sum=0

for i in range(1,n):
    if n%i==0:
        sum+=i  
    
if sum==n:
    print(f"{n}, This is perfect number!")
else:
    print(f"{n}, This is not a perfect number!")
