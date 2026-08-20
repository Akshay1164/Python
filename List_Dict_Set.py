# List comprehension in Python
print("List comprehension in Python")
square = [x**2 for x in range(10) if x%2 ==0]
print (square)

List1 = [1, 2, 3, 4, 5]
List2 = [x*2 for x in List1]
print (List2)

print("Dictionary comprehension in Python")
# Dictionary comprehension in Python
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict2 = {key: value*2 for key, value in dict1.items()}
print(dict2)

price_map = {'apple':100, 'grape':80}
discount = {k:v*0.8 for k,v in price_map.items()}
print(discount)

#set comprehension in Python
print("Set comprehension in Python")

unique_length = {len(x) for x in ['apple', 'grapes', 'banana']}
print(unique_length)