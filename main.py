import os
# Шпаргалка по python
# https://proglib.io/p/samouchitel-po-python-dlya-nachinayushchih-chast-3-tipy-dannyh-preobrazovanie-i-bazovye-operacii-2022-10-14
# на подумать https://itproger.com/course/python/5
"""
# 1.1 - базовые типы данных
print(3, type(3), "это целочисленное")  # int/integer - целочисленное 3
print(4.2, type(4.2), "это вещественное")  # float - с плавающей точкой (десятичная дробь)
print(True, type(True), "это логическое")  # bool/boolean - логическое
print("Я изучаю Python", type("Я изучаю Python"))  # str/string - строка
# 1.2составные типы данных - собственная классификация
print([3, 15, 9, 20, "стопицот"], type([3, 15, 9, 20, "стопицот"]), "это список")  # list - список
print({"Вася": "10", "Петя": "90", "Толя": "3"}, type({"Вася": "10", "Петя": "90", "Толя": "3"}), "это словарь")  # dict/dictionary - словарь
# 2.1 - переменные (нельзя начинать с числа) + демонстрация динамической типизации
a = 3
print(a, type(a))
a = True
print(a, type(a))
"""

# 2.2 перепишем 1.1 с использованием переменных
var_int = 6
var_float = 5.1
var_bool = True
var_str = "Хелло ворлд"
var_list = [var_int, var_float, var_bool, var_str]
print(var_int, type(var_int), "целое")
print(var_float, type(var_float), "вещественное")
print(var_bool, type(var_bool), "логическое")
print(var_str, type(var_float), "строковое")
print(var_list, type(var_list), "список")
# {'жанр': 'драма', 'рейтинг': 8.5, 'название': 'Зеленая миля'}
var_dict = {"целое": var_int, "вещественное": var_float, "логическое": var_bool, "строковое": var_str, "список": var_list}
print(var_dict, "словарь")

# 3.1 операции с данными - числа
result_add = var_int + var_int  # + это сложение addition
result_sub = var_int - var_float  # - это вычитание subtraction
result_mul = var_int * var_int  # * это умножение multiplying
result_div = var_float / var_int  # / это деление division
print(var_int, "+", var_int, "=", result_add)
print(var_int, "-", var_float, "=", result_sub)
print(var_int, "*", var_int, "=", result_mul)
print(var_float, "/", var_int, "=", result_div)

# 3.2 текст
text_add = var_str + " добавленный текст"  # + это конкатенация (сложение)
text_mul = var_str * 5  # * это репликация(умножение)
print(text_add)
print(text_mul)

# 3.3 операции с данными - списки
print()
var_list.append("добавленное значение") # append - добавление элемента списка
print(var_list)
print(var_list[0])  # получение элемента по индексу
var_list[0] = "измененный нулевой элемент"  # перезапись значений по индексу
print(var_list)
var_list.pop(0)  # удаление элемента по индексу
print(var_list)
print(len(var_list))  # длина списка

# 3.4 операции с данными - словари
print("исходный словарь - ", var_dict)
print(var_dict["логическое"])  # получение значения по ключу
var_dict["новый ключ"] = "новое значение"  # изменение и добавление значения в словарь
print(var_dict)
var_dict["новый ключ"] = "значение 2"
print(var_dict)
del var_dict["новый ключ"]  # удаление элемента
print(var_dict)
# условные операторы if, elif, else

if True:
    pass
elif True:
    pass
else:
    pass
# логические операторы
# ==
# >
# <
# !=
# and
# or
# not


# ЭХО
# input_data = input()
# print(input_data)
# циклы for,while
#while True:
    #pass

#for # определенное количество раз\

#for in # итератор объекта
# особенности range (start,stop,step)

while True:
    print("---===Узнать квадрат числа===---")
    print(int(input("Введите число:\n"))**2, "для продолжения нажмите enter")
    input()
    os.system("CLS")

# камень-ножницы-бумага
