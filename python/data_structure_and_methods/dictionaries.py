from sys import getsizeof

point = {"x": 1, "y": 2}
point = dict(x=1, y=2)
point["x"] = 10
point["z"] = 20
print(point)
# error handling if the value in dict
if "a" in point:
    print(point["a"])
print(point.get("a", 0))
del point["x"]
print(point)

for key in point:
    print(point[key])

for key, value in point.items():
    print(key, value)

# expression comperhension
# [expression for item in items]
values = {x: x*2 for x in range(5)}
print(values)

# generator object
valuess = (x * 2 for x in range(1000))
print("gen", getsizeof(valuess))
# print(len(valuess))
valuess = [x * 2 for x in range(1000)]
print("gen", getsizeof(valuess))

# large dataset use generator expression.
# no len because not stored

# unpacking operator // spread
numbers = [1, 2, 3]
print(numbers)
print(*numbers)
print(1, 2, 3)

# can unpack any iterable
values = [*range(5), *"hello"]
print(values)

# unpack dictionaries
first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 1}
print(combined)
