square = lambda x: x ** 2
print(square(5))  # 25

data = [("a", 3), ("b", 1), ("c", 2)]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)
# [('b', 1), ('c', 2), ('a', 3)]