from functools import reduce
def multiply_list(numbers):
    result = reduce(lambda x, y: x * y, (numbers))
    return result

my_list = [2,4,5,6,7]

print(multiply_list(my_list))

