class grandfather:
    gold=0
    house=0

    def g_getdata(self):
        self.gold=input("Enter Gold Details:")
        self.house=input("Enter House Details:")

class father(grandfather):
    car=0
    bal=0

    def f_getdata(self):
        self.car=input("Enter Car Details:")
        self.bal=input("Enter Bank Balance Details:")

class son(father):
    def alldetails(self):
        print("Gold:",self.gold)
        print("House:",self.house)
        print("Car:",self.car)
        print("Balance:",self.bal)

sn=son()
sn.g_getdata()
sn.f_getdata()
sn.alldetails()
