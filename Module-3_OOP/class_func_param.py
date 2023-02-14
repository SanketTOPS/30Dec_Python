class studinfo:
    stid=1
    stnm='Nirav'

    def getdata(self):
        print("Student ID:",self.stid)
        print("Student Name:",self.stnm)
    
st=studinfo()
st.getdata()