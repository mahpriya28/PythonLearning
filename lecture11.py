#lamba functions -> anonymous functions, functions without a name, one liner
#syntax -> lambda arguments: expression

square = lambda x:x*x
print(square(5))
numbers=[1,2,3,4,5]
squared_numbers = map(lambda x:x*x, numbers)
print(list(squared_numbers))
#filter function -> filters elements from a list based on a condition
even_numbers = filter(lambda x:x%2==0, numbers)
print(list(even_numbers))
#reduce function -> reduces a list to a single value by applying a binary function cumulatively
from functools import reduce
product = reduce(lambda x,y:x*y, numbers)
print(product)
#sorting with lambda
points = [(1,2), (3,1), (5,0), (2,4)]
points.sort(key=lambda point:point[1])
print(points)
#using lambda with other functions
def apply_function(func, value):
    return func(value)
result = apply_function(lambda x:x*2, 5)
print(result)
#lambda functions in data structures
operations = {'add': lambda x,y:x+y,
              'subtract': lambda x,y:x-y,
              'multiply': lambda x,y:x*y}
print(operations['add'](5,3))
print(operations['subtract'](5,3))
print(operations['multiply'](5,3))

