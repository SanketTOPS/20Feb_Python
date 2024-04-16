class student:
    stid=12
    stnm="Sanket"

    def printdata(self):
        print("ID:",self.stid)
        print("Name:",self.stnm)


#Object of class
"""st=student()
st.printdata()
st.stid=20
st.stnm="Ashok"
st.printdata()"""


#Instance of class
student().printdata()
student().stid=23
student().stnm="Jay"
student().printdata()
