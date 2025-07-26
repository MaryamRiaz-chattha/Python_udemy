# Higher-order function returning a function
def make_adder(x):
    def adder(y):
        return x + y
    return adder

add5 = make_adder(5)
print(add5(3))  # Output: 8
def say_hello(name):
    return f"Hello, {name}!"

def greet(func, name):
    return func(name)

print(greet(say_hello, "Maryam"))  # Output: Hello, Maryam!
