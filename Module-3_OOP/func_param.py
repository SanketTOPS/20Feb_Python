class studinfo:
    stid=1
    stnm="Sanket"

    def getsum(self,a,b):
        print("Sum:",a+b)


st=studinfo()
print("ID:",st.stid)
print("Name:",st.stnm)

st.getsum(32,77)