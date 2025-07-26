# 🧠 Python Variable Naming Rules — Notes Style with Code Examples

# 1️⃣ A variable name must start with a letter or an underscore (_)
# ✅ Good:
name = "Ali"
_name = "Fatima"

# ❌ Bad:
# 1name = "Error!"  # ❌ Starts with a number - not allowed

# 2️⃣ A variable name cannot start with a number
# ✅ Correct:
roll1 = 123

# ❌ Incorrect:
# 5roll = 321  # ❌ Invalid: cannot start with a digit

# 3️⃣ Variable names can only include letters, numbers, and underscores (_)
user_name1 = "Sara"  # ✅ valid
# user-name = "Nope"  # ❌ dash is not allowed
# user@name = "Nope"  # ❌ symbols like @, !, etc. are not allowed

# 4️⃣ Variable names are case-sensitive
age = 25
Age = 30
# 'age' and 'Age' are two different variables in Python

# 5️⃣ Avoid using Python **reserved keywords** (like if, for, class, etc.)
# ❌ Invalid examples:
# if = "condition"
# class = "student"

# ✅ Use something meaningful instead:
condition_if = "condition"
student_class = "A"

# 6️⃣ Use clear and descriptive names for readability
# ❌ Bad:
x = 10
y = 20

# ✅ Good:
student_marks = 95
total_subjects = 5

# 7️⃣ Follow **snake_case** convention (all lowercase + underscores between words)
student_name = "Amina"
user_age = 20

# 8️⃣ Constants (values that shouldn't change) are written in UPPERCASE
PI = 3.1416
MAX_USERS = 100

# 9️⃣ No special characters (!, @, #, etc.) allowed in variable names
# ❌ Invalid:
# user!name = "No" 
# my#value = "Wrong"

# 1️⃣0️⃣ Spaces are NOT allowed in variable names
# ❌ Invalid:
# full name = "Ahmed"
# ✅ Use:
full_name = "Ahmed"

# ✅ In short:
# Start with a letter or underscore
# Use letters, numbers, and underscores only
# Case matters: student and Student are different
# Don’t use spaces or special symbols
# Don’t use Python's own keywords



# string, integer,float,boolean,list,tuple
name = "Maryam" 
print(name)  # Output: Maryam
age = 25
print(age)  # Output: 25
is_student = True
print(is_student)  # Output: True
fruits = ["apple", "banana", "cherry"]
print(fruits)  # Output: ['apple', 'banana', 'cherry']
coordinates = (4, 5)
print(coordinates)  # Output: (4, 5)
name = "Maryam Riaz"
age = 26
height = 5.9
is_graduate = True
skills = ["Python", "HTML", "CSS"]

print(f"My name is {name}, I am {age} years old, my height is {height}, and I know {skills}")
