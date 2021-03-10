# find
letters = ["a", "b", "c"]
if "b" in letters:
    print(letters.index("b"))
# if doesnt exist, give error not -1, jadi di cond in

# sort
numbers = [3, 51, 25, 4, 9]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

print(sorted(numbers))
print(sorted(numbers, reverse=True))

items = [
    ("prod1", 1033),
    ("prod2", 112),
    ("prod3", 31),
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)
items.sort(key=sort_item, reverse=True)
print(items)
