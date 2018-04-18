countEven=0
countOdd=0
a = []
n = int(input("Number of items you want to add: "))
for i in range(0,n):
    a.append(int(input("Enter your items: ")))
    if(a[i]>=0):
        if a[i] % 2 == 0:
            countEven+=1
        else:
            countOdd+=1
    else:
        int(input("Please reenter your number: "))
print("Number of even numbers: ",countEven)
print("Number of odd numbers: ",countOdd)

