class student:
    def getdata(self,stid,stnm):
        print("ID:",stid)
        print("Name:",stnm)


st=student()
#st.getdata(12,'Ashok') #static

id=input("Enter your ID:")
nm=input("Enter your Name:")

st.getdata(id,nm)