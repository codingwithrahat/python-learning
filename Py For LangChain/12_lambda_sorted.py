#sorted fucntion is 

value = [
    (1, 'b', 'banana'),
    (2, 'a', 'apple'),
]

#item is a tuple and we want to sort by second element of the tuple
def sort_by_second_element(item):
    return item[1]

sorted_value = sorted(value, key=sort_by_second_element)
print(sorted_value)  # Output: [(2, 'a', 'apple'), (1, 'b', 'banana')]

#using lambda function to sort by second element
sorted_value_lambda = sorted(value, key = lambda x : x[1])