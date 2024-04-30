data=[2,3,8,6,9,5,8,7]

sublist=[30,8,7] 
res=False


if set(sublist).intersection(set(data))==set(sublist):
    res=True
else:
    res=False

print("Is there sublist?:",res)