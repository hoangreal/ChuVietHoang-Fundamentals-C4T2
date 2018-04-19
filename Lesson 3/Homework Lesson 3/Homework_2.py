attempts = 0
while True :
    response = input("Do you want to quit? (y/n): ")
    attempts += 1
    if response == "y" or response == "n":
        if response=="y":
            break
    else:
        print("Incorrect Letter")
print("Exiting after", attempts, "attempts")




