# ✅ Python For Loop 

# 1️⃣ Loop through a list
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

print("-----")

# 2️⃣ Loop through a string
for letter in "Hello":
    print(letter)

print("-----")

# 3️⃣ Using range() to loop numbers from 0 to 4
for i in range(5):
    print("i =", i)

print("-----")

# 4️⃣ Loop with start, end, and step
for i in range(1, 10, 2):  # Start from 1 to 9, step by 2
    print("Step loop:", i)

print("-----")

# 5️⃣ for loop with else block
for i in range(3):
    print("i =", i)
else:
    print("Loop finished.")

print("-----")

# 6️⃣ Break: Exit loop early
for fruit in fruits:
    if fruit == "banana":
        break
    print("Break Example:", fruit)

print("-----")

# 7️⃣ Continue: Skip current iteration
for fruit in fruits:
    if fruit == "banana":
        continue
    print("Continue Example:", fruit)

print("-----")

# 8️⃣ Nested loop example
colors = ["red", "green"]
items = ["shirt", "hat"]

for color in colors:
    for item in items:
        print(color, item)


# Example of a for loop in Python

# Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)

print("\n--- Looping through dictionary ---")

# Loop through a dictionary
person = {
    "name": "Alice",
    "age": 25,
    "city": "Lahore"
}

# Loop through keys (default)
for key in person:
    print("Key:", key)

# Loop through values
for value in person.values():
    print("Value:", value)

# Loop through key-value pairs
for key, value in person.items():
    print(f"Key: {key} => Value: {value}")
