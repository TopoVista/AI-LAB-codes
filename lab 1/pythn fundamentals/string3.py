# Using f-strings for basic string interpolation
name = "Alice"
greeting = f"Hello, {name}!"
print(greeting)

# Using f-strings with expressions
age = 30
message = f"{name} is {age} years old."
print(message)

# Formatting numbers with f-strings
pi = 3.14159
formatted_pi = f"Pi rounded to two decimal places: {pi:.2f}"
print(formatted_pi)

# Using f-strings with dictionaries
person = {"name": "Bob", "age": 25}
info = f"{person['name']} is {person['age']} years old."
print(info)

# Using f-strings with lists
fruits = ["apple", "banana", "cherry"]
fruit_list = f"My favorite fruits are: {', '.join(fruits)}."
print(fruit_list)

# Using f-strings for multi-line strings
multi_line = f"""Name: {name}
Age: {age}
Favorite fruit: {fruits[0]}"""
print(multi_line)

# Using f-strings with function calls
def get_greeting(name):
    return f"Welcome, {name}!"

print(get_greeting("Charlie"))