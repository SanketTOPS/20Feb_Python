a=56

print("A:",a)

def getvalue():
    global a
    a=90
    print("A is:",a)

getvalue()