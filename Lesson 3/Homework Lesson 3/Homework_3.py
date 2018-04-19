def find_kmers(string, n):
    kmers = []
    lenght = len(string)

    for i in range(0, n - n + 1):
        kmers.append(string[i:i + n])

    return kmers
n = int(input("Enter your number: "))
a = find_kmers("ABCDE",n)
print(a)