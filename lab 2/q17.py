#write a program to print the sum of digits of a number
number = input("Enter a number: ")
sum_of_digits = 0
for digit in number:
    sum_of_digits += int(digit)
print(f"The sum of digits in {number} is {sum_of_digits}.")  

#method 2 - using while loop
number = int(input("Enter a number: ")) 
if number < 0:
    number = -number 
sum_of_digits = 0
temp = number
while temp > 0:
    digit = temp % 10
    sum_of_digits += digit
    temp //= 10
print(f"The sum of digits in {number} is {sum_of_digits}.")  