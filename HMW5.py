# class hookah:
#     def __init__(self, manufacturer, name, material, height):
#         self.__manufacturer = manufacturer           # уровень доступа protected
#         self._name = name                            # уровень доступа private
#         self.material = material
#         self.height = height
#
#     def smoke(self):
#         return 'Its smokes nicely!'
#
#     def get_manufacturer(self):
#         return f'hello! manufacturer is {self.__manufacturer}'
#
#     def set_manufacturer(self, new_manufacturer):
#         self.__manufacturer = new_manufacturer
#
#     def get_name(self):
#         return f'hello! name is {self._name}'
#
#     def set_name(self, new_name):
#         self._name = new_name
#
# hookah = hookah('DS', 'Galaxy', 'glass/stailess steel', '70cm')
#
# print(hookah.__dict__)
# print(hookah._hookah__manufacturer)
# print(hookah.get_manufacturer())
# print(hookah.get_name())
# print(hookah.material)
# print(hookah.height)
# print(hookah.smoke())
#
# print(hookah.set_name('Stainless 3'))
# print(hookah.get_name())
#
# print(hookah.set_manufacturer('H3'))
# print(hookah.get_manufacturer())
#
# print(hookah.set_manufacturer('AlphaHookah'))
# print(hookah.get_manufacturer())

# проверка проверка
# ветка
# из гита
# еще строчка

class Person():
    def __init__(self, imya, familya, otchestvo, god_rojdenia):
        self.imya = imya
        self.familya = familya
        self.otchestvo = otchestvo
        self.god_rojdenia = god_rojdenia

class Student(Person):
    def __init__(self, imya, familya, otchestvo, god_rojdenia, facultet, list_scores, teacher):
        super().__init__(imya, familya, otchestvo, god_rojdenia)
        self.facultet = facultet
        self.list_scores = list_scores
        self.teacher = teacher

    def set_score(self, new_score):
        self.list_scores.append(new_score)

    def avg_scores(self):
        print(sum(self.list_scores)/len(self.list_scores))

class Teacher(Person):
    def __init__(self, imya, familya, otchestvo, god_rojdenia, subject, salary, q_of_students):
        super().__init__(imya, familya, otchestvo, god_rojdenia)
        self.subject = subject
        self.salary = salary
        self.q_of_students = q_of_students

    def get_students(self):
        print(f'препод {self.familya} с зп {self.salary} обучает {self.q_of_students}')

student1 = Student('Ivan', 'Petrov', 'Pavlovich', '2001', 'ATP', [4, 5, 4], 'Gorohov')
prepod1 = Teacher('Petr', 'Gorohov', 'Inavovich', '1990', 'programming', 10000, 100)

print(student1.list_scores)
prepod1.get_students()
student1.set_score(1)
print(student1.list_scores)
print(student1.avg_scores())