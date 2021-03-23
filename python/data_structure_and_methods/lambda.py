# lambda function / anon func / HOF
from collections import deque
items = [
    ("prod1", 1033),
    ("prod2", 112),
    ("prod3", 31),
]

items.sort(key=lambda item: item[1])
print(items)

# map

# di list in biar karena map return iterable object map
prices = list(map(lambda price: price[1], items))
print(prices)

filtered = list(filter(lambda price: price[1] > 40, items))
print(list(map(lambda item: item[1], filtered)))

# map but with list comperhension
# WOOOOOOW PYTHON
# [expression for item in items]
prices = [item[1] for item in items]
print(prices)

filtered = [item[1] for item in items if item[1] > 40]
print(filtered)

zipped = list(zip(prices, filtered))
print(zipped)

queue = deque([])
queue.append('a')
queue.append('b')
queue.append('c')
queue.popleft()
print(queue)
