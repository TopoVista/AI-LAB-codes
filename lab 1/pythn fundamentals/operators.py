# Arithmetic Operators
print(10 + 5)      # Addition: 15
print(10 - 3)      # Subtraction: 7
print(4 * 3)       # Multiplication: 12
print(15 / 3)      # Division: 5.0
print(17 % 5)      # Modulus: 2
print(2 ** 3)      # Exponentiation: 8
print(15 // 4)     # Floor Division: 3

# Comparison Operators
print(10 > 5)      # Greater than: True
print(10 == 10)    # Equal to: True
print(5 != 3)      # Not equal: True
print(3 < 8)       # Less than: True

# Logical Operators
print(True and False)   # AND: False
print(True or False)    # OR: True
print(not True)         # NOT: False
print((5 > 3) and (2 < 4))  # AND with conditions: True

# Assignment Operators
x = 10             # Simple assignment
y = 5
x += 3             # x = x + 3: x is now 13
y -= 2             # y = y - 2: y is now 3

# Membership Operators
list1 = [1, 2, 3]
print(2 in list1)      # in: True
print(5 not in list1)  # not in: True

# Identity Operators
a = [1, 2, 3]
b = a
print(a is b)      # is: True
print(a is not [1, 2, 3])  # is not: True

# Bitwise Operators
print(5 & 3)       # AND: 1
print(5 | 3)       # OR: 7
print(5 ^ 3)       # XOR: 6
print(~5)          # NOT: -6
print(5 << 1)      # Left shift: 10
print(5 >> 1)      # Right shift: 2