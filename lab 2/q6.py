#write a program to find the largest among three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
largest = a
if b > largest:
    largest = b
if c > largest:
    largest = c
print(f"The largest among {a}, {b} and {c} is {largest}")
    