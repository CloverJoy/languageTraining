from array import array

pointtype = 1, 2, 3
point = (1, 2, 3, 4, 5) * 3
point = tuple("hello world")
print(point[0:2])
print(type(pointtype))
if 1 in point:
    print('hurray')

x = 10
y = 11

a = 1
b = 2

temp = a
a = b
b = temp

print(a)
print(b)

# because of the tuple
x, y = y, x

print("x", x)
print("y", y)

# tuple inmutable.

# if too much list, use array for performance
# google python typecode
# must same type
numbers = array("i", [1, 2, 3])
numbers.append(4)
numbers.insert(0, 0)
print(numbers)

# sets. collection no dupe
numbers = [1, 1, 2, 3, 4, 4, 5]
first = set(numbers)
second = {1, 5}

# union
print(first | second)
# intersection
print(first & second)
# difference
print(first - second)
# sem different
print(first ^ second)

if 1 in first:
    print('found')
