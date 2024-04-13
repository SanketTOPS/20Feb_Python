class studinfo:
    def getdata(self,id,name):
        print("ID:",id)
        print("Name:",name)
    
st=studinfo()
#st.getdata(1,'Sanket') #static


stid=input("Enter an ID:")
stnm=input("Enter your Name:")

st.getdata(stid,stnm)