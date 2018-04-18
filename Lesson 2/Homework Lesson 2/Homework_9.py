m = int(input("Enter your row: "))
n = int(input("Enter your column: "))
a=[[0 for j in range(n)] for i in range(m)] #Create a 2D array
for i in range(m):
    for j in range(n):
        a[i][j] = i*j
print(a)
