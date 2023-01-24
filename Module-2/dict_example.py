stdata={'id':1,'name':'sanket','sub':'python'}
"""print(stdata)
print(stdata.keys())
print(stdata.values())
print(stdata['name'])
print(stdata.get('sub'))"""

"""if 'sanket' in stdata.values():
    print("Yes...")
else:
    print("Noo")"""

#print(len(stdata))

#stdata['id']=2


"""for i in stdata:
    print(i)"""

"""for i in stdata.values():
    print(i)"""

"""for i in stdata.items():
    print(i)"""

stdata['city']='rajkot'
#stdata.pop('name')
#stdata.clear()
#del stdata
#print(stdata)

newdict=stdata.copy()
print(newdict)