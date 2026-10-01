n = int(input("Enter N: "))

arr = []

for i in range(n):
    num = int(input("Enter number: "))
    arr.append(num)

result = []

for num in arr:
    if num != 0:
        result.append(num)

for num in arr:
    if num == 0:
        result.append(num)

print("Original array =", arr)
print("After moving zeros =", result)