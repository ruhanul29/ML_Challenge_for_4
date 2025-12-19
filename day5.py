#micro-1

numbers_list = list(range(1,10001))

numbers_set = set (numbers_list)

n = 5000

print ((n-1) in numbers_list)
print((n-1) in numbers_set)

#Explanation - 
#As set/dict uses a "hash table",so python creates hash value and use it to jump directly to the memory location.
#In the case of set/dict there is no need of scanning each element which is needed in list.
#So time complexity of set/dict is O(1) and for list is O(N)
#Thats why, "set/dict" is faster than "list"

#micro-2

user = {"id": 1}

email = user.get("email")
print(email)

#micro-3

word = "banana"
freq = {}

for char in word:
    if char in freq:
        freq[char] += 1
    else: 
        freq[char] = 1
print(freq)        

#micro-4

defaults = {"theme": "light","audio": "on"}

user_pref = {"theme": "dark"}

merged = defaults.copy()
merged.update(user_pref)

print(merged)