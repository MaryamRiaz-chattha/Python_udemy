# ✅ Basic if statement
age = 18

if age >= 18:
    print("You are eligible to vote.")

# ✅ if-else statement
age = 16

if age >= 18:
    print("You can vote.")
else:
    print("You are too young to vote.")

# ✅ if-elif-else statement
marks = 75

if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
else:
    print("Grade: C or below")

# ✅ Nested if statement
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed.")
    else:
        print("ID required.")
else:
    print("Too young to enter.")

# ✅ Short-hand if
a = 10
b = 5

if a > b: print("a is greater")

# ✅ One-line if-else (ternary operator)
print("a is greater") if a > b else print("b is greater")

# ✅ Using logical operators (and, or)
username = "admin"
password = "123"

if username == "admin" and password == "123":
    print("Login successful.")
else:
    print("Login failed.")
