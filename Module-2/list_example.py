mylist=['Python','JAVA','PHP','Node','Android']

"""print(mylist)
print(mylist[0])
print(mylist[-1])
print(mylist[0:3])
print(mylist[3:])
print(mylist[:4])
print(len(mylist))"""

"""if 'C++' in mylist:
    print("Yes...")
else:
    print("Nooo")"""

#mylist[2]='iOS'
#print(mylist)

"""for i in mylist:
    print(i)"""

# --------------------------------------------------------- #
print(mylist)
#mylist.append("C")
mylist.insert(1,'C')
#mylist.pop()
#mylist.pop(2)
#mylist.remove('Python')
#mylist.clear()
#mylist.reverse()
#mylist.sort()
#del mylist
#print(mylist)


#newlist=mylist.copy()

newlist=['C++','DS','HTML','CSS']
print(newlist)

#print(mylist+newlist)
mylist.extend(newlist)
print(mylist)