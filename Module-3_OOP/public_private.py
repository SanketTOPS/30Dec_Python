class student:
    __stid=12
    __stnm="Sanket"

    def __getdata(self):
        print("This is getdata")
    
    def __printdata(self):
        print(self.__stid)
        print(self.__stnm)
    
    def studdata(self): #public
        self.__printdata()

st=student()
#print(st.stid)
#print(st.stnm)
#st.getdata()

#st.printdata()

st.studdata()