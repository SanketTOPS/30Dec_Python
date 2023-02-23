# User define Function 

def getdata():
    global id
    global name
    global sub
    id=input('Enter ID: ')
    name=input('Enter Name: ')
    sub=input('Enter Subject: ')


def printdata():
    print('ID: ',id)
    print('Name: ',name)
    print('Subject: ',sub)

getdata()
printdata()    