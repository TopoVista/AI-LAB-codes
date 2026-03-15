# Program to swap two numbers using a temporary variable
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(f"Before swap: a = {a}, b = {b}")
temp = a
a = b
b = temp
print(f"After swap: a = {a}, b = {b}")