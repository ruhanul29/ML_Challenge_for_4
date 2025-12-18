#micro-1

a = [1,2,3]
b = a

b[0] = 99
print(a)

#micro-2

data = [10,20,30,40,50]

new = data[-1:-4:-1]

print(new)

#micro-3

a = []

a.append(1)
a.append(2)
a.append(3)

last_number = a.pop()
print(last_number)

#micro-4

i = [x**2 for x in range (1,11) if x%2 == 0]
print(i)