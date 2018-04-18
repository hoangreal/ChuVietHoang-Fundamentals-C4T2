import random
n = random.randint(1,9)
m = int(input("Enter your guess: "))
while(n != m):
    m = int(input("Enter your guess: "))
print("Well guess!")