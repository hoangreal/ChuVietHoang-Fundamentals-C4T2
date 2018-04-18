result = []
a = input("Enter your sequence: ")
new = [x for x in a.split(',')]  #remove the ',' in a and store the new sequence in variable "new"
for i in new:
    x = int(i) #Convert str to int
    if x%5==0:
        result.append(i)
print(','.join(result)) #add the ',' after having results