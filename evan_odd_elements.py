n = int(input("Enter N: "))

arr = []

for i in range(n):
    num = int(input("Enter number: "))
    arr.append(num)

even = 0
odd = 0

for num in arr:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers =", even)
print("Odd numbers =", odd)