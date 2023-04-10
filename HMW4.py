# 4.1

# a = int(input('введите сторону квадрата: '))
# def sqare(a):
#     return a * 4, a * a, (2**0.5) * a
# print(sqare(a))

# 4.2

# def person(**kwargs):
#     for key, value in kwargs.items():
#         print(key, ':', value)
#     return kwargs
# print(person(age=20, name='anna', last_name='ivanova'))

# 4.3

# my_list = [20, -3, 15, 2, -1, -21]
# print(list(filter(lambda x: x > 0, my_list)))

# 4.4

# from functools import reduce
# my_list = [20, -3, 15, 2, -1, -21]
# result = reduce(lambda x, y: x * y, my_list)
# print(result)

# 4.5

# import time
#
# def time_of_function(func):
#     def wrapped(arg):
#         start_time = time.perf_counter_ns()
#         res = func(arg)
#         print(time.perf_counter_ns() - start_time)
#     return wrapped
#
# @time_of_function
# def say_hello(name):
#     print(f'hello {name}')
#
# say_hello('sam')

# 4.6

# from my_calc import *
# print(plus(1, 2))
# print(minus(1, 2))
# print(umnog(1, 2))
# print(delenie(1, 2))