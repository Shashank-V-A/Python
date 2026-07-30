numbers = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x : x % 2 == 0, numbers))
print(result)

from functools import reduce
numbers = [10, 20, 30, 40]
result = reduce(lambda x, y: x + y, numbers)
print(result)