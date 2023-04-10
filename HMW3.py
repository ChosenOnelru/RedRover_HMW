# 3.1

# my_list = ['a', 'b', [1, 2, 3], 'd']
# print(my_list[0-2])

# 3.2

# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# result  = list([item for item in list_1 if isinstance(item, int)])
# print(sum(result))
# result1 = list([item for item in list_1 if isinstance(item, str)])
# print(*filter(lambda x: 'a' in x, result1))

# 3.3

# my_list = ['cat', 'dog', 'horse', 'cow']
# print(tuple(my_list))

# 3.4

# family1 = list(map(str, input("введите состав семьи 1 через запятую: ").split(', ')))
# family2 = list(map(str, input("введите состав семьи 2 через запятую: ").split(', ')))
# if len(family1) > len(family2):
#     print('семья 1 больше')
# elif len(family1) == len(family2):
#     print('Equal')
# else:
#     print('семья 2 больше')

# 3.5

# film = dict(title='matrix', director='vachowsky', year='1998', budget=40000000, main_actor='reeves', slogan='none')
# print(film.keys())
# print(film.values())
# print(film)

# 3.6

# my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# print(sum(my_dictionary.values()))

# 3.7

# list1 = [1, 2, 3, 4, 5, 3, 2, 1]
# print(set(list1))

# 3.8

# set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
# set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
# list3 = (set1.difference(set2), set2.difference(set1))
# print(set1.intersection(set2))
# print(set1.issubset(set2))
# print(set2.issubset(set1))
# print(f'значения, которые не встречаются в обоих множествах: {list3}')