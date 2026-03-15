#write a program to check if a number is single digit , double digit or three digit
number = int(input("Enter a number: "))
if 0 <= number <= 9:
    print(f"{number} is a single digit number.")
elif 10 <= number <= 99:
    print(f"{number} is a double digit number.")
elif 100 <= number <= 999:
    print(f"{number} is a three digit number.")
else:
    print(f"{number} has more than three digits.")    