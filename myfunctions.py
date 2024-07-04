#~ USAGE
# cd c:\python_developer
# cd d:\python_developer
# .\pydev\Scripts\activate
# cd c:\python_developer\lesson_04
# cd d:\python_developer\lesson_04
#~~~~~~~~~~~~~~~~~~~~~~~~
# python myfunctions.py
#~~~~~~~~~~~~~~~~~~~~~~~~

  
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
МОДУЛЬ 1
В модуле прописаны заготовки для 8 функций
Под каждой функцией есть описание как она должна работать
ниже есть примеры использования функции
Задание: реализовать код функции, чтобы он работал по описанию и примеры использования давали верный результат
"""

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ 1
def simple_separator():
  """
  Функция создает красивый резделитель из 10-и звездочек (**********)
  :return: **********
  """
  # pass
  return '*' * 10

print('1 '+'~'*70)
print(simple_separator() == '**********')  # True

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ 2
def long_separator(count):
  """
  Функция создает разделитель из звездочек число которых можно регулировать параметром count
  :param count: количество звездочек
  :return: строка разделитель, примеры использования ниже
  """
  # pass
  return '*' * count

print('2 '+'~'*70)
print(long_separator(3) == '***')  # True
print(long_separator(4) == '****')  # True

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ 3
def separator(simbol, count):
  """
  Функция создает разделитель из любых символов любого количества
  :param simbol: символ разделителя
  :param count: количество повторений
  :return: строка разделитель примеры использования ниже
  """
  # pass
  return simbol * count

print('3 '+'~'*70)
print(separator('-', 10) == '----------')  # True
print(separator('#', 5) == '#####')  # True

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ 4
def hello_world():
  """
  Функция печатает Hello World в формате:
  **********

  Hello World!

  ##########
  :return: None
  """
  # pass
  print("**********\n\nHello World!\n\n##########")

print('4 '+'~'*70)
'''
**********

Hello World!

##########
'''
hello_world()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ 5
def hello_who(who='World'):
  """
  Функция печатает приветствие в красивом формате
  **********

  Hello {who}!

  ##########
  :param who: кого мы приветствуем, по умолчанию World
  :return: None
  """
  # pass
  print("**********\n\nHello {}!\n\n##########".format(who))

print('5 '+'~'*70)
'''
**********

Hello World!

##########
'''
hello_who()
'''
**********

Hello Max!

##########
'''
hello_who('Max')
'''
**********

Hello Kate!

##########
'''
hello_who('Kate')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ 6
def pow_many(power, *args):
  """
  Функция складывает любое количество цифр и возводит результат в степень power (примеры использования ниже)
  :param power: степень
  :param args: любое количество цифр
  :return: результат вычисления # True -> (1 + 2)**1
  """
  # pass
  result = sum(args)  # Суммируем все переданные аргументы
  return result ** power  # Возводим результат в указанную степень

print('6 '+'~'*70)
print(pow_many(1, 1, 2) == 3)  # True -> (1 + 2)**1 == 3
print(pow_many(1, 2, 3) == 5)  # True -> (2 + 3)**1 == 5
print(pow_many(2, 1, 1) == 4)  # True -> (1 + 1)**2 == 4
print(pow_many(3, 2) == 8)  # True -> 2**3 == 8
print(pow_many(2, 1, 2, 3, 4) == 100)  # True -> (1 + 2 + 3 + 4)**2 == 10**2 == 100

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ 7
def print_key_val(**kwargs):
  """
  Функция выводит переданные параметры в фиде key --> value
  key - имя параметра
  value - значение параметра
  :param kwargs: любое количество именованных параметров
  :return: None
  """
  # pass
  for key, value in kwargs.items():
    print(f"{key} --> {value}")

print('7 '+'~'*70)
"""
name --> Max
age --> 21
"""
print_key_val(name='Max', age=21)
"""
animal --> Cat
is_animal --> True
"""
print_key_val(animal='Cat', is_animal=True)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ 8
def my_filter(iterable, function):
  """
  (Усложненое задание со *)
  Функция фильтрует последовательность iterable и возвращает новую
  Если function от элемента последовательности возвращает True, то элемент входит в новую последовательность иначе нет
  (примеры ниже)
  :param iterable: входаня последовательности
  :param function: функция фильтрации
  :return: новая отфильтрованная последовательность
  """
  # pass
  return [element for element in iterable if function(element)]

print('8 '+'~'*70)
print(my_filter([1, 2, 3, 4, 5], lambda x: x > 3) == [4, 5])  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x == 2) == [2])  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x != 3) == [1, 2, 4, 5])  # True
print(my_filter(['a', 'b', 'c', 'd'], lambda x: x in 'abba') == ['a', 'b'])  # True
