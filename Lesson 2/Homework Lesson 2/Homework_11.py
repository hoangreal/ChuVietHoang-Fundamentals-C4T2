s = input("Input a string: ")
countLetter = 0
countDigit = 0
for i in s:
    if i.isdigit(): #Check whether the string contains a digit
        countDigit+=1
    elif i.isalpha(): #Check whether the string contains an alphabetical letter
        countLetter+=1
    else:
        continue
print("Letters", countLetter)
print("Digits", countDigit)