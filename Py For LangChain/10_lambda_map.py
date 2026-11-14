
#map function with lambda
#map funtion does what?
#it take a list or tupple and applies a operation to each element of the list or tupple and returns a map object

num = [1, 2, 3, 4, 5]

def square(x):
    return x * x

squared_num = list(map(square, num))
print(squared_num)  # Output: [1, 4, 9, 16, 25]

#using lambda function with map
squared_num_lambda = list(map(lambda x: x * x, num))
print(squared_num_lambda)  # Output: [1, 4, 9, 16, 25]