class studinfo:
    stid=1
    stnm='Nirav'

    def getdata(self):
        print("Student ID:",self.stid)
        print("Student Name:",self.stnm)


# calling via object
"""st=studinfo()
st.getdata()
st.stid=2
st.stnm='Ashok'
st.getdata()"""

# calling via instance
studinfo().getdata()
studinfo().stid=2
studinfo().stnm='Sanket'
studinfo().getdata()