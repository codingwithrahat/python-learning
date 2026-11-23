# normal function
def normal_function():
    return [1, 2, 3, 4]

print(normal_function())  # Output: [1, 2, 3, 4] print at a time


#generator function
def generator_function():
    for i in range(1, 5):
        yield i

print(generator_function())  # Output: <generator object generator_function at 0x...>

# it call generate object to get the value one at a time instead of all at once
for value in generator_function():
    print(value)  # Output: 1, 2, 3, 4 (one at a time)


#anotehr way

obj = generator_function()
print(next(obj))  # Output: 1
print(next(obj))  # Output: 2


