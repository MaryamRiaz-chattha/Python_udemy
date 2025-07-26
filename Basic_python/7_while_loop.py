   # WHILE LOOP IN PYTHON

# Basic concept:
# A while loop keeps running **as long as** the condition is True.
number = 1


while number <= 5:
    print("Number is:", number)
    number = number + 1  

 

# Example 1: Counting from 1 to 5
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1  # Increment the count to avoid infinite loop

print("\n--- Example 2: Exit with user input ---")

# Example 2: Keep asking name until user types 'exit'
user_input = ""
while user_input != "exit":
    user_input = input("Type your name (or type 'exit' to stop): ")
    if user_input != "exit":
        print("Hello,", user_input)

print("\nLoop has ended.")


