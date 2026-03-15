#write a program to find the smallest among three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
smallest = a
if b < smallest:
    smallest = b
if c < smallest:
    smallest = c
print(f"The smallest among {a}, {b} and {c} is {smallest}")    