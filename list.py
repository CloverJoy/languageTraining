# # basic
# letters = ["a", "s", "d"]
# matrix = [[0, 1], [0, 2], [0, 3]]
# zeros = [0] * 5
# combo = zeros + letters
# print(zeros)
# print(combo)  # WOW PYTHON

numbers = list(range(20))
# print(numbers)

# split = list("hello world")
# print(len(split))

# # slicing / splicing
# print(split[0:3])
# # every index 2
# print(split[::2])
# # reverse array
# print(split[::-1])

# list unpacking (kind of destructure array)
# nums = [0, 1, 2]
# first, second, third = nums
# firstt, secondd, thirdd, *other = numbers
# first, *other, last = numbers
# print(first, second, third)
# print(other)

# loop
# for number in numbers:
#     print(number)

letters = ["a", "b", "c", "d"]

# enumerate create tuple read only
# for letter in enumerate(letters):
#     print(letter[0], letter[1])

# items = (0, "a")
# index, letter = items
# for index, letter in enumerate(letters):
#     print(index, letter)

# add remove list
# push
letters.append('pushed')
# unshift
letters.insert(0, 'unshifted')
# pop
letters.pop()
# can push index number for specific remove
# if multiple, first time appear remove
print(letters)
# remove sesuai isi
letters.remove("c")
print(letters)
# clear semuanya
letters.clear()
print(letters)
