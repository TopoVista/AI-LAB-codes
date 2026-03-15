# Python Booleans - True and False

# Basic boolean values
is_active = True
is_deleted = False

# Comparisons return booleans
x = 10
y = 5
print(x > y)  # True
print(x == y)  # False
print(x < y)  # False
print(x != y)  # True
print(x >= y)  # True
print(x <= y)  # False

# Logical operators
a = True
b = False
print(a and b)  # False
print(a or b)   # True
print(not a)    # False
print(not b)    # True

# String comparisons
name = "Alice"
print(name == "Alice")  # True
print(name != "Bob")    # True
print(len(name) > 3)    # True

# Membership tests
items = [1, 2, 3, 4, 5]
print(3 in items)       # True
print(10 in items)      # False
print(10 not in items)  # True

# Type checking
value = 42
print(isinstance(value, int))    # True
print(isinstance(value, str))    # False

# Truthiness (values that evaluate to True/False)
print(bool(1))          # True
print(bool(0))          # False
print(bool("hello"))    # True
print(bool(""))         # False
print(bool([1, 2]))     # True
print(bool([]))         # False
print(bool(None))       # False

# Conditional statements using booleans
if is_active:
    print("User is active")

if not is_deleted:
    print("User is not deleted")