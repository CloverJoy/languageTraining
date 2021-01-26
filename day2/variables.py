# Day 2: 30 days of python programming
# var declaration
first_name = 'Clover'
last_name = 'Joy'
full_name = 'CloverJoy'
country = 'USA'
city = 'Lynnwood'
age = 25
year = 2021
is_married = False
is_true = True
is_light_on = True
waifu, bias, stan, is_python_good = 'Sagiri', 'Seulgi', 'IZ*ONE', True

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(age))
print(type(bias))
print(len(first_name))
print(len(first_name) > len(last_name))

# another var declare + operation
num_one, num_two = 5, 4
_total = num_one + num_two
print(_total)
_diff = num_one - num_two
_product = num_one * num_two
_division = num_one / num_two
_modulus = num_one % num_two
_exp = num_one ** num_two
_floor = num_one // num_two
# input must be string. must convert
radius = int(input('enter radius'))
print('The radius', radius * radius)
# some of the built in method
print(list(bias))
print(float(_modulus))
# reserved keywords
help('keywords')
