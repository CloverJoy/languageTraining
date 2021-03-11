from timeit import timeit
# # for handling error
# try:
#     # with this, no need to finally
#     with open("app.py") as file:
#         print("File opened.")
#         # .__enter .__exit
#     age = int(input("Age: "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError) as ex:
#     print("You didnt enter a valid age")
#     print(ex)
#     print(type(ex))
# else:
#     print("No exceptions were thrown")
# # finally:
# #     # always excecuted. good for closing file
# #     file.close()
# print("Excecution continues.")

# to check exec time
code1 = """def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age

try: 
    calculate_xfactor(-1)
except ValueError as error:
    print(error)
"""

# raise exception slower performance if large and scalability matter
print("first code =", timeit(code1, number=10000))


# not recommended raise exception
