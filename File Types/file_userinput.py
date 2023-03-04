fl=open("newfile.txt","a")


n=int(input("Enter number of students:"))

for i in range(n):
    id=input("Enter ID:")
    name=input("Enter Name:")

    fl.write(f"ID:{id}\n")
    fl.write(f"Name:{name}\n")