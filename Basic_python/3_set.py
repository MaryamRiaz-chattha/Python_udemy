# Creating a set
my_set = {1, 2, 3, 4, 5}
print("Original set:", my_set)

# ✅ No duplicate values allowed
my_set = {1, 2, 2, 3, 4, 4}
print("Set with duplicates:", my_set)  # Output: {1, 2, 3, 4}

# ✅ Add items to a set
my_set.add(6)
print("After adding:", my_set)

# ✅ Remove an item
my_set.remove(2)
print("After removing 2:", my_set)

# ✅ Fast membership test
if 4 in my_set:
    print("4 is in the set")

# ✅ Set operations
a = {1, 2, 3}
b = {3, 4, 5}

print("Union:", a | b)           # {1, 2, 3, 4, 5}
print("Intersection:", a & b)    # {3}
print("Difference:", a - b)      # {1, 2}
print("Symmetric Difference:", a ^ b)  # {1, 2, 4, 5}