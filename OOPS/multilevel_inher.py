class ajay:
    aid=0
    asub=""
    def a_getdata(self):
        self.aid=input("Enter Ajay's ID:")
        self.asub=input("Enter Ajay's Subject:")
    
class nirav(ajay):
    nid=0
    nsub=""
    def n_getdata(self):
        self.nid=input("Enter Nirav's ID:")
        self.nsub=input("Enter Nirav's Subject:")

class ashok(nirav):
    asid=0
    assub=""
    def as_getdata(self):
        self.asid=input("Enter Ashok's ID:")
        self.assub=input("Enter Ashok's Subject:")

class tops(ashok):
    def printdata(self):
        print("--------Ajay--------")
        print("Ajay's ID:",self.aid)
        print("Ajay's Subject:",self.asub)
        print("--------Nirav--------")
        print("Nirav's ID:",self.nid)
        print("Nirav's Subject:",self.nsub)
        print("--------Ashok--------")
        print("Ashok's ID:",self.asid)
        print("Ashok's Subject:",self.assub)


tp=tops()
tp.a_getdata()
tp.n_getdata()
tp.as_getdata()
tp.printdata()
