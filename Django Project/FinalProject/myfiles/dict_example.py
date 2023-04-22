stdata={'id':12,'name':'sanket','sub':'python'}

"""print(stdata)
print(stdata['name'])
print(stdata['id'])
print(stdata.get('sub'))
print(len(stdata))"""

#print(stdata)
#print(stdata.keys())
#print(stdata.values())

"""if 'name' in stdata:
    print("Yes...")
else:
    print("Error!")
"""

"""if 'python' in stdata.values():
    print("Yes...")
else:
    print("Noo")"""


# ----------------------------------------------- #

#print(stdata)
#stdata['id']=30


"""for i in stdata:
    print(i)"""

"""for i in stdata.values():
    print(i)"""

"""for i in stdata.items():
    print(i)"""

# Key=id and Value=12
# Key=name and Value=sanket

"""for i,j in stdata.items():
    print(f"Key={i} and Value={j}")"""

# ----------------------------------------- #

print(stdata)
stdata['city']='Rajkot'
#stdata.pop('id')
#del stdata['name']
stdata.clear()
print(stdata)
