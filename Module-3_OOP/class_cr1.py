class stud:
    stid=101
    stnm="Sanket"

    def myfunc(self):
        print("This is stud class method!")


#Object of class
st=stud()
print("ID:",st.stid)
print("Name:",st.stnm)
st.myfunc()
