try:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    print("Sum:",a+b)
except Exception as e:
    #print("Error!")
    print(e)
else:
    print("This is Finally block!")

