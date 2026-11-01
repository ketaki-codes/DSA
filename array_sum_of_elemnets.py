n = int(input("Enter N: "))

arr = []

for i in range(n):
    num = int(input("Enter number: "))
    arr.append(num)

total = sum(arr)

print("Sum =", total)

