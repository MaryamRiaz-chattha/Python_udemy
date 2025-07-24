# ✅ List Example (Mutable)
# Lists are mutable - you can change, add, or remove elements

fruits_list = ["apple", "banana", "mango"]
print("Original List:", fruits_list)

# Changing the second item
fruits_list[1] = "orange"
print("After Changing:", fruits_list)

# Adding a new item
fruits_list.append("grape")
print("After Adding:", fruits_list)

# Removing an item
fruits_list.remove("apple")
print("After Removing:", fruits_list)


print("\n-----------------------\n")

# ✅ Tuple Example (Immutable)
# Tuples are immutable - once created, they cannot be changed

fruits_tuple = ("apple", "banana", "mango")
print("Original Tuple:", fruits_tuple)

# Trying to change the second item will cause an error
 #fruits_tuple[1] = "orange"  # TypeError: 'tuple' object does not support item assignment

#  You also cannot add or remove items from a tuple
# fruits_tuple.append("grape")     # AttributeError
# fruits_tuple.remove("apple")     # AttributeError

# Tuples are useful when data should not change
