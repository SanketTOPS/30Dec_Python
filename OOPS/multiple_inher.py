class ajay:
    aid=0
    asub=""
    def a_getdata(self):
        self.aid=input("Enter Ajay's ID:")
        self.asub=input("Enter Ajay's Subject:")
    
class nirav:
    nid=0
    nsub=""
    def n_getdata(self):
        self.nid=input("Enter Nirav's ID:")
        self.nsub=input("Enter Nirav's Subject:")

class ashok:
    aid=0
    asub=""
    def a_getdata(self):
        self.aid=input("Enter Ashok's ID:")
        self.asub=input("Enter Ashok's Subject:")

class tops(ajay,nirav,ashok):
    def printdata(self):
        print("--------Ajay--------")
        print("Ajay's ID:",self.aid)
        print("Ajay's Subject:",self.asub)
        print("--------Nirav--------")
        print("Nirav's ID:",self.nid)
        print("Nirav's Subject:",self.nsub)
        print("--------Ashok--------")
        print("Ashok's ID:",self.aid)
        print("Ashok's Subject:",self.asub)


tp=tops()
tp.a_getdata()
tp.n_getdata()
tp.a_getdata
tp.printdata()
