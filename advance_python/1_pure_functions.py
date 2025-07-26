# ✅ Pure Function
# Just adds two numbers and gives the result
def add(a, b):
    return a + b

print(add(1, 2))  # 3
print(add(4, 5))  # 9


# ❌ Impure Function
# Changes something outside the function
count = 0

def increase():
    global count
    count += 1
    return count

print(increase())  # 1
print(increase())  # 2 (changes each time)
