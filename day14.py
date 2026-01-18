# # micro-1

# def two_sum (nums, target):
#     seen = {} 
#     for current in nums:
#         needed = target - current
#         if needed in seen:
#             return needed, current
#         seen[current] = True
#     return None    

# nums = [3,5,6,8]
# target = 11

# print(two_sum(nums, target))

# #micro-2

# def is_pailndrome(s):
#     clean_s =s.replace(" ","").lower()
#     return clean_s == clean_s [::-1]

# text_1= "Do or Die"
# print(is_pailndrome(text_1))

# text_1= "Are you alright jhon."
# print(is_pailndrome(text_1))

# #micro -3

# def are_anagrams(b1,b2):
#     b1_clean = b1.replace (" ","").lower()
#     b2_clean = b2.replace (" ","").lower()
    
#     return sorted(b1_clean) == sorted(b2_clean)

# print(are_anagrams("silent", "listen"))
# print(are_anagrams("hello","world"))

# # micro-4

# def flatten(lst):
#     result = []
#     for item in lst:
#         if isinstance(item,list):
#             result.extend(flatten(item))
#         else:
#             result.append(item)
#     return result                

# nested = [1,[2,[3,4]]]
# flat = flatten(nested)
# print(flat)

# micro - 5

# def FizzBuzz(i=1, max_i=100):
#     if i>max_i:
#         return
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:    
#         print("Buzz")
#     else:
#         print(i) 
#     FizzBuzz(i + 1, max_i) 

# FizzBuzz()      

#micro6-10......