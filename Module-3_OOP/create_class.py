class studinfo:
    stid=1
    stnm='Nirav'

    def getdata(self):
        print("This is getdata function")
    
    def getsum(self,a,b):
        print("Sum:",a+b)


st=studinfo() #object
print(st.stid)
print(st.stnm)
st.getdata()
st.getsum(23,56)
