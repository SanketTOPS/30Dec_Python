fl=open('new.txt','r+')

print(fl.read())
#print(fl.readline())
#print(fl.readlines())
#print(fl.readlines()[4])

fl.write("\nGood Morning")

"""if fl.readable():
    print("Yes...")
    print(fl.read())
else:
    print("Error!File is not readable")"""

"""for i in fl:
    print(i)"""