#write a program to find the factorial of a number
number = int(input("Enter a number: "))
factorial = 1
for i in range(1, number + 1):
    factorial *= i  
print(f"The factorial of {number} is {factorial}.")