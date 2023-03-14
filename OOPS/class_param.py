class student:
    def getdata(self,id,name):
        print("ID:",id)
        print("Name:",name)

st=student()
#st.getdata(101,'Sanket')
stid=input("Enter ID:")
stnm=input("Enter Name:")
st.getdata(stid,stnm)