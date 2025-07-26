def double(x):
    return x * 2

numbers = [1, 2, 3, 4, 5]

result = map(double, numbers)  # double function har number par chalega
print(list(result))  # Output: [2, 4, 6, 8, 10]
