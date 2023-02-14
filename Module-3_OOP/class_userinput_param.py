class studinfo:
    def getdata(self,stid,stnm):
        print("Student ID:",stid)
        print("Student Name:",stnm)


st=studinfo()
#st.getdata(101,'Sanket')

id=input("Enter ID:")
name=input("Enter Name:")
st.getdata(stid=id,stnm=name)