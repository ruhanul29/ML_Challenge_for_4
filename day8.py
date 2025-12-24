#micro-1

List = list(range(10000000))

if -5 in List:
    print("Element founded")
else:
    print("Element not founded")    
    
#micro-2

List = list(range(10000000))

a = set (List)

print(-5 in a)

#micro-3

a =[]

a.append(50)

a.insert(0,50)

print(a)

#micro-4

x = [1,2,3,4,5]

x.pop()

x.pop(0)

print(x)

#micro-5

chars = []

for _ in range (10000):
    chars.append("a")
s = "".join(chars)       
print(s)

#micro-6

t = list(range(1000000)) #asume 1 billion
print(len(t))

#micro-7

list_1 = [1,2,3,4,5,6,7]
list_2 = [6,7,8,9,10]

duplicates = []

for item_1 in list_1:
    for item_2 in list_2:
        if item_1 == item_2:
             duplicates.append(item_1)
print(duplicates)             

#micro-8

import random

a = [random.randint(1,100) for _ in range(10)]

print("Original list: ", a)

a.sort()
print("Sorted list: ", a)

#micr-9

#.......

#micro-10 

x = list(range(5001))

slice_x = x[1000:2001]
print(slice_x[:10])