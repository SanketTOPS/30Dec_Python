#fl=open('new.txt','w')
fl=open('new.txt','a') #append mode

id=input("Enter ID:")
name=input("Enter Name:")

#fl.write(id)
#fl.write(name)


fl.write(f"ID:{id}\nName:{name}\n")