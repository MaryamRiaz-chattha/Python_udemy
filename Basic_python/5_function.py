def function_name():
    # block of code
    print("Hello from a function!")
#  # ✅ Calling the function 
function_name()  
# ✅ function return value
def add(a, b):
    return a + b

result = add(5, 3)
print("Sum is:", result)  # Output: Sum is: 8
# ✅ Function with parameters
def greet(name="Guest"):
    print("Hello,", name)

greet()           # Output: Hello, Guest
greet("Zainab")   # Output: Hello, Zainab

# ✅ Function with multiple parameters
def student_info(name, age, grade):
    print("Name:", name)
    print("Age:", age)
    print("Grade:", grade)

student_info("Ayesha", 16, "10th")
