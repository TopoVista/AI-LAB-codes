#write a program to print the multiplication table of any number
number = int(input("Enter a number: "))
print(f"Multiplication table of {number}:") 
for i in range(1, 13):
    product = number * i
    print(f"{number} x {i} = {product}")