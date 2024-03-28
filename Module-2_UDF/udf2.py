def getdata(id,name,sub):
    print("ID:",id)
    print("Name:",name)
    print("Subject:",sub)

n=int(input("Enter number of students:")) #n=10

for i in range(n):
    #getdata(1,'Sanket','Python')
    
    stid=input("Enter an ID:")
    stnm=input("Enter a Name:")
    stsub=input("Enter a Subject:")
    getdata(stid,stnm,stsub)