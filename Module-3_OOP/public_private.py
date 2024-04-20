class student:
    __stid=101 #private
    __stnm="Sanket" #private

    def __myfunc(self):
        print("This is default method of t his class!")
        print("ID:",self.__stid)
        print("Name:",self.__stnm)
    

    def getdata(self):
        self.__myfunc()


st=student()
#print(st.stid)
#print(st.stnm)
#st.myfunc()
st.getdata()
