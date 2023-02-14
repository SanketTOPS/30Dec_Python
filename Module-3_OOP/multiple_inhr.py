class nirav:
    nid=0
    nsub=''

    def n_getdata(self):
        self.nid=input("Enter Nirav's ID:")
        self.nsub=input("Enter Nirav's Subject:")

class ashok:
    aid=0
    asub=''

    def a_getdata(self):
        self.aid=input("Enter Ashok's ID:")
        self.asub=input("Enter Ashok's Subject:")

class sanket:
    sid=0
    ssub=''

    def s_getdata(self):
        self.sid=input("Enter Sanket's ID:")
        self.ssub=input("Enter Sanket's Subject:")


class tops(nirav,ashok,sanket):
    def printdata(self):
        print("---------Nirav's Data--------")
        print("Nirav's ID:",self.nid)
        print("Nirav's Subject:",self.nsub)
        print("---------Ashok's Data--------")
        print("Ashok's ID:",self.aid)
        print("Ashok's Subject:",self.asub)
        print("---------Sanket's Data--------")
        print("Sanket's ID:",self.sid)
        print("Sanket's Subject:",self.ssub)
    
tp=tops()
tp.n_getdata()
tp.a_getdata()
tp.s_getdata()
tp.printdata()