from collections import namedtuple

# TUPLES IN PYTHON - FROM EASY TO HARD

# ============================================
# THEORY: What is a Tuple?
# ============================================
# A tuple is an immutable (unchangeable) collection of ordered elements
# enclosed in parentheses (). Unlike lists, tuples cannot be modified after creation.
# Tuples are faster and use less memory than lists.
# Tuples can contain any data type: integers, strings, lists, even other tuples.

# ============================================
# EASY LEVEL
# ============================================

# 1. Creating a simple tuple
simple_tuple = (1, 2, 3, 4, 5)  # Basic tuple with integers
print("Simple tuple:", simple_tuple)

# 2. Tuple with mixed data types
mixed_tuple = (1, "hello", 3.14, True)  # Tuples can hold different types
print("Mixed tuple:", mixed_tuple)

# 3. Accessing tuple elements (indexing)
fruits = ("apple", "banana", "orange")
print("First fruit:", fruits[0])  # Accessing first element (index starts at 0)
print("Last fruit:", fruits[-1])  # Negative indexing gets from end

# 4. Tuple unpacking
coordinates = (10, 20, 30)
x, y, z = coordinates  # Unpacking: assign each element to a variable
print(f"Coordinates - x: {x}, y: {y}, z: {z}")

# ============================================
# INTERMEDIATE LEVEL
# ============================================

# 5. Slicing tuples (getting a range of elements)
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
sliced = numbers[2:7]  # Elements from index 2 to 6 (7 is excluded)
print("Sliced tuple:", sliced)

# 6. Tuple methods - count() and index()
colors = ("red", "blue", "green", "red", "red")
red_count = colors.count("red")  # count() returns how many times element appears
blue_index = colors.index("blue")  # index() returns position of first occurrence
print(f"Red appears {red_count} times, Blue is at index {blue_index}")

# 7. Nested tuples (tuple containing tuples)
matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print("Nested tuple:", matrix)
print("Element at [1][2]:", matrix[1][2])  # Access nested element

# 8. Converting list to tuple and vice versa
my_list = [1, 2, 3, 4]
converted_tuple = tuple(my_list)  # Convert list to tuple
print("Converted to tuple:", converted_tuple)

back_to_list = list(converted_tuple)  # Convert tuple back to list
print("Converted back to list:", back_to_list)

# ============================================
# HARD LEVEL
# ============================================

# 9. Tuple comprehension (generator expression converted to tuple)
squares = tuple(x**2 for x in range(1, 6))  # Create tuple of squares
print("Squares tuple:", squares)

# 10. Sorting tuples with multiple elements
students = (("Alice", 85), ("Bob", 92), ("Charlie", 78))
sorted_students = sorted(students, key=lambda x: x[1])  # Sort by score (index 1)
print("Sorted by score:", sorted_students)

# 11. Using tuple as dictionary key (tuples are hashable, lists are not)
location_data = {
    (10, 20): "Location A",
    (30, 40): "Location B",
    (50, 60): "Location C"
}
print("Dictionary with tuple keys:", location_data[(10, 20)])

# 12. Unpacking with * operator (extended unpacking)
data = (1, 2, 3, 4, 5)
first, *middle, last = data  # Unpack first, last, and rest into middle
print(f"First: {first}, Middle: {middle}, Last: {last}")

# 13. Named tuples (creating structured data)
Point = namedtuple('Point', ['x', 'y', 'z'])
p = Point(10, 20, 30)
print(f"Named tuple - x: {p.x}, y: {p.y}, z: {p.z}")

# 14. Comparing tuples (lexicographic comparison)
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 4)
tuple3 = (1, 2, 3)
print(f"tuple1 < tuple2: {tuple1 < tuple2}")  # True (3 < 4)
print(f"tuple1 == tuple3: {tuple1 == tuple3}")  # True (all elements equal)

# 15. Immutability demonstration
immutable_tuple = (1, 2, 3)
try:
    immutable_tuple[0] = 10  # This will raise an error
except TypeError as e:
    print(f"Error (expected): {e}")  # Tuples cannot be modified!