# - no return, just task. // return none
def greet(x):
    print(f"hello there {x}")
    print("hello world!")

# - retun something


def sum_me(x, y):
    return x+y


number = sum_me(2, 2)
print(number)

# keyword argument y =
message = sum_me("hello", y=" chris")
print(message)

file = open("context.txt", "w")
file.write(message)

# default args


def increment(number, by=1):
    return number + by


print(increment(2, 5))
print(increment(2))

# xargs


def multiply(*numbers):
    result = 1
    for number in numbers:
        result *= number
    return result


print(multiply(2, 3, 4))

# xxargs args multiple key value pairs


def save_user(**user):
    print(user)


save_user(name="John", id=1, age=22)

# scoping
message = "a"

print(message)


def change_global():
    global message
    message = "b"
    # bad practice


change_global()
print(message)
