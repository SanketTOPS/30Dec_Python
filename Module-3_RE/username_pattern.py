import re

#Sanket2020
username=input("Enter Username:")

unm_pattern="[A-Z]+[a-z]+[0-9]"

x=re.findall(unm_pattern,username)

if x: #true
    print("Username is valid!")
else:
    print("Error! Invalid Username")