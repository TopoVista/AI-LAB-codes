#write a program to check if three numbers form a triangle or not
a = int(input("Enter first side length: "))
b = int(input("Enter second side length: "))
c = int(input("Enter third side length: "))
if a + b > c and a + c > b and b + c > a:
    print(f"The lengths {a}, {b}, and {c} can form a triangle.")
else:
    print(f"The lengths {a}, {b}, and {c} cannot form a triangle.")
