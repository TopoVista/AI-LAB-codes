# ===== EASY =====
# 1. Create and access lists
fruits = ["apple", "banana", "orange"]
print(fruits[0])  # apple
print(fruits[-1])  # orange

# 2. List methods
numbers = [3, 1, 4, 1, 5]
numbers.append(9)  # Add element
numbers.sort()  # Sort in place
print(numbers)

# 3. List slicing
items = [1, 2, 3, 4, 5]
print(items[1:4])  # [2, 3, 4]
print(items[::-1])  # Reverse

# ===== MEDIUM =====
# 4. List comprehension
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

# 5. Nested lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][2])  # 6

# 6. List unpacking
a, b, c = [10, 20, 30]
print(a, b, c)

# ===== HARD =====
# 7. Advanced list comprehension with conditions
evens = [x for x in range(20) if x % 2 == 0]
print(evens)

# 8. Nested list comprehension
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print(matrix)

# 9. Flatten nested list
nested = [[1, 2], [3, 4], [5, 6]]
flat = [item for sublist in nested for item in sublist]
print(flat)  # [1, 2, 3, 4, 5, 6]

# 10. Complex operations
data = [5, 2, 8, 1, 9, 3]
result = sorted(set(data), reverse=True)
print(result)  # [9, 8, 5, 3, 2, 1]