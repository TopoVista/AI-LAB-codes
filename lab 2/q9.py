#write a program to check if a triangle is equilateral, isosceles or scalene
a = int(input("Enter first side length: "))
b = int(input("Enter second side length: "))
c = int(input("Enter third side length: "))
if a == b == c:
    print("The triangle is equilateral.")
elif a == b or b == c or a == c:
    print("The triangle is isosceles.")
else:
    print("The triangle is scalene.")