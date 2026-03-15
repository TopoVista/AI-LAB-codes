# Method 1: Using the + operator
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)  # Output: Hello World

# Method 2: Using f-strings (recommended)
name = "Alice"
age = 25
result = f"My name is {name} and I am {age} years old"
print(result)  # Output: My name is Alice and I am 25 years old

# Method 3: Using .format()
result = "The {} is {}".format("sky", "blue")
print(result)  # Output: The sky is blue

# Method 4: Using .join()
words = ["Python", "is", "awesome"]
result = " ".join(words)
print(result)  # Output: Python is awesome

# Method 5: String multiplication
result = "Ha" * 3
print(result)  # Output: HaHaHa