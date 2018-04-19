#Create a random list of tuples with random item in each tuples
nTuple = int(input("Enter your number of Tuple: "))
nItem = int(input("Enter your number of Tuple's item: "))
TupleList=[() for x in range(nTuple)]
for i in range(nTuple):
    for j in range(nItem):
        add = int(input("Enter your item: "))
        TupleList[i] += (add,)

#Change the last Tuple's item of a list to a random number
n = int(input("Your desired number: "))
for i in range(nTuple):
    Object_List = list(TupleList[i])
    Object_List[-1] = n
    TupleList[i] = tuple(Object_List)
print(TupleList)




