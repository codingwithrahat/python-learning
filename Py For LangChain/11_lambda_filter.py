num = [1, 2, 3, 4, 5]

# Filter even numbers
# if even number is found then it will return true and that number will be added to the new list
def is_even(n):
    return n % 2 == 0

even_num = list(filter(is_even, num))

print(even_num)  # Output: [2, 4]


#using lambda function to filter even numbers
even_num_lambda = list(filter(lambda n: n % 2 == 0, num))