#micro-1

add = lambda x, y: x+y
print(add(3,6)) 

#micro-2

num = [1,2,3,4,5]

squared = list(map(lambda x: x**2, num))

print(squared)

#micro-3

numb = [1 ,-3,6,-8,-4,9,-2]

pos_num = list(filter(lambda x: x>= 0, numb))

print(pos_num)

#micro-4

from functools import reduce
import operator

numbers = [10,20,30,40]

product = reduce(operator.mul, numbers)

print(product)

#micro-5

items = ["100px","20px","3px"]

sorted_items = sorted(items, key=lambda x: int(x.rstrip("px")))

print(sorted_items)

#micro-6

names = ["A","B"]
ages = [20,30]

result = dict(zip(names,ages))

print(result)

micro-7

....

#micro-8

numbers = [-5,-7,-9,-3]

is_neg = any(n < 0 for n in numbers)

is_pos = any(n > 0 for n in numbers)

print("Any negetive?", is_neg)
print("Any posetive?", is_pos)

#micro-9

from functools import partial

def power (base, exp):
    return base**exp

square = partial(power, exp=2)

print(square(3))
print(square(4))
print(square(8))      

#micro-10

number = [(1,2),(3,4),(5,6)]

def modify(x):
    x[0] = x[0] * 10
    return x

try:
    result = list (map(modify, number))
    print(result)
except TypeError as e:
    print("Error: ", e)    