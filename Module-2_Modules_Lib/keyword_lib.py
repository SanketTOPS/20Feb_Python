import keyword

x=keyword.kwlist
print(x)

n=1
for i in x:
    print(i, "=",n)
    n+=1