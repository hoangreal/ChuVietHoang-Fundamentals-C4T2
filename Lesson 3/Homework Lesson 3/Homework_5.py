def selection_sort(list): #Find the minimum number in each stage of a list
    for i in range(len(list)):
        min = list[i]
        for j in range(i+1,len(list)):
            if list[j] < list[i]:
                list[i],list[j] = list[j],list[i]
    return list

n = int(input("Enter your number of item in a list: "))
list = []
for i in range(n):
    list.append(int(input("Enter your number: ")))
a = selection_sort(list)
print(a)