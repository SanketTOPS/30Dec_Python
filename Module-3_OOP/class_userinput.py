class studinfo:
    stid:int
    stnm:str

    def getdata(self):
        self.stid=input("Enter ID:")
        self.stnm=input("Enter Name:")
    
    def printdata(self):
        print("Student ID:",self.stid)
        print("Student Name:",self.stnm)

st=studinfo()
st.getdata()
st.printdata()


