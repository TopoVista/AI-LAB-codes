def swap_without_thirdVar(a,b):
    a = a + b
    b = a - b
    a = a - b
    return a,b

if __name__ == "__main__":
    a = 6
    b = 7
    print(f"before swapping: a = {a} , b = {b}")
    a,b = swap_without_thirdVar(a,b)
    print(f"after swapping: a = {a} , b = {b}")
            