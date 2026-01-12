#micro-1
def gen():
    yield 1
    yield 2
    yield 3
for value in gen():
    print(value)
    
#micro-2

import sys

list_comp = [i for i in range (1000000)]
list_expr = (i for i in range (1000000))      

print("List comp size: ", sys.getsizeof(list_comp))
print("Generator expr size: ", sys.getsizeof(list_expr))    

#micro-3

def fibonacci():
    a,b = 0,1
    while True:
        yield a 
        a, b = b, a+b
gen = fibonacci()

for _ in range(10):
    print(next(gen))
    
#micro-4    

def g():
    yield 1
    yield 2
    yield 3

gen = g()

for x in gen:
    print(x)
print("Second loop: ")    

for x in gen:
    print(x)
            
#micro-5

def g():
    yield 1
    yield 2
    yield 3

gen = g()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen)) # StopIteration

#micro-6

def square(nums):
    for n in nums:
        yield n*n
def even_only(nums):
    for n in nums:
        if n % 2 == 0:
            yield n

nums = range(10) 

gen = even_only(square(nums))

for value in gen:
    print(value)                   


#micro-7        

def fake_file():
    line_number = 0
    while True:
        yield f"Line {line_number}: simulated data chunk\n"
        line_number += 1

gen = fake_file()

for _ in range(5):
    print(next(gen))  

#micro-8      

def gen1():
    yield 1
    yield 2
    yield 3

def gen2():
    yield 10
    yield 20
    yield 30

def combined_gen():
    yield from gen1()
    yield from gen2()
    
for value in combined_gen():
    print(value)    
       
#micro-9

def echo():
    while True:
        recived = (yield)
        print(f"Received: {recived}")  

gen = echo()

next(gen)

gen.send('I')
gen.send("am")
gen.send("Ruhanul")        

#micro-10

def run_avg():
    total = 0
    count = 0
    avg = None
    while True:
        num = (yield avg)  
        if num is None:
            
            continue
        count += 1
        total += num
        avg = total/count

gen = run_avg()

next(gen)

print(gen.send(10))        
print(gen.send(20))
print(gen.send(30))
print(gen.send(40))

        
    