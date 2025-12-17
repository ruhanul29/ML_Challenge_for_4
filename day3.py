#micro-1

while True:
    password = input('Enter password: ')
    if password == "Stop":
       print("Loop stopped")
       break
   
#micro-2

a = int(input("Enter a number: "))   
sum = 0
for i in range(1, a+1):
    sum = sum + i
print("Sum is: ",sum)    

#micro-3

for i in range (1,11):
    if i == 5:
        continue
    print(i)
 
#micro-4        

word = "DATA"

for i in word:
    print(i)