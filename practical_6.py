# 6. Write a Python Program to Check Armstrong Number.

n = int(input("Enter a number: "))
# initialize the sum
s = 0
t = n

while t > 0:
    digit = t % 10
    s += digit ** 3
    t //= 10

# display the result
if n == s:
    print(n, "is an Armstrong number")
else:
    print(n, "is not an Armstrong number")
