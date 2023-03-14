class student:
    __stid=12
    __stnm="Sanket"

    def __getdata(self):
        print("ID:",self.__stid)
        print("Name:",self.__stnm)
    
    def printdata(self): #public
        self.__getdata()


st=student()
st.printdata()