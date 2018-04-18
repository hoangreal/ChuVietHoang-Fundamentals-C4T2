import re #We will use the function "search" in library "re" in order to find keywords
p= input("Input your password: ")
count = 0
while count == 0 :
    if (len(p)<6 or len(p)>12):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[$#@]",p):
        break
    elif re.search("\s",p):
        break
    else:
        print("Valid Password")
        count+=1
        break

if count == 0:
    print("Not a Valid Password")