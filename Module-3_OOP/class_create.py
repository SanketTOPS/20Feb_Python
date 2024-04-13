class studinfo:
    stid=21
    stnm="Sanket"

    def getdata(self):
        print("This is Studinfo class.")


#Object of class
st=studinfo()

print("ID:",st.stid)
print("Name:",st.stnm)

st.getdata()