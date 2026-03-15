#write a program to count how many digits are present in a number
number = input("enter a number: ")
count = 0   
for digit in number:
    count += 1  
print(f"The number of digits in {number} is {count}.")


#method 2 - diving the number by 10 until it becomes 0
number = int(input("Enter a number: "))
count = 0
temp = number
while temp > 0:
    temp //= 10
    count += 1
print(f"The number of digits in {number} is {count}.")

#method 3 - using string conversion
number = int(input("Enter a number: ")) 
count = len(str(number))
print(f"The number of digits in {number} is {count}.")