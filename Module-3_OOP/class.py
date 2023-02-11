class student:
    stid=12
    stnm='Sanket'

    def getdata(self):
        print("This is getdata from student")
    
    def getsum(self,a,b):
        print("Sum:",a+b)

# object of class
st=student()
print("ID:",st.stid)
print("Name:",st.stnm)
st.getdata()
st.getsum(12,34)


