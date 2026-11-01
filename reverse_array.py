n = int(input("Enter N: "))

arr = []

for i in range(n):
    num = int(input("Enter number: "))
    arr.append(num)

reverse = arr[::-1]

print("Original array =", arr)
print("Reverse array =", reverse)