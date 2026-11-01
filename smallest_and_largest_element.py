n = int(input("Enter N: "))

arr = []

for i in range(n):
    num = int(input("Enter number: "))
    arr.append(num)

unique = list(set(arr))
unique.sort()

print("Smallest =", unique[0])
print("Second Smallest =", unique[1])
print("Largest =", unique[-1])
print("Second Largest =", unique[-2])