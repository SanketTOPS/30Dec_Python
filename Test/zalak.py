# Collection types
#List  - 5
#Tuple
#Set - 5
#Dict - 5


mylist=["python","java","c++","ios"]
print(mylist[0])
print(mylist[:3])
print(mylist.pop(2))
if "python" in mylist:
    print("yes...")
else:
    print("no...")



mytup=('truck','bus','car','bike')
print(mytup)


myset={'a','b','c','d','e'}

print(myset.remove('c'))
print(myset.update('h','i','j'))
print(len(myset))
print(myset.pop())


mydic={'id':'1','name':'zalak','sub':'python'}
print(mydic.keys())
print(mydic.values())
print(mydic.items())
for i in mydic.items():
    print(i)


































 