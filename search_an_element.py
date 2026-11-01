n = int(input("Enter N: "))

arr = []

for i in range(n):
    num = int(input("Enter number: "))
    arr.append(num)

search = int(input("Enter number to search: "))

if search in arr:
    print("Number is present")
    print("Position =", arr.index(search) + 1)
else:
    print("Number is not present")