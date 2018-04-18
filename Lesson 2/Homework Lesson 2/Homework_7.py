a=[0,1]
for i in range(2,50):
    m = a[i-2]+a[i-1]
    a.append(m)
for i in range(0,50):
    if a[i] <= 50:
        print(a[i],end=" ")
