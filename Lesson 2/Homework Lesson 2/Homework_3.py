a=[]
for x in range(1500, 2702):
    if x%7==0 and x%5==0:
        a.append((x))
for x in range(0,len(a)):
    if x != len(a)-1:
        print(a[x],end=",")
    else:
        print(a[x],end=" ")