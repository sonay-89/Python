my_dog = ("1" "2" "3")
print(len(my_dog))
my_dogs = len("1" "2" "3")
print(my_dogs)
# Булев тип данных True -истина, False - ложь (не заключаем в кавычки, так как это ключевые слова)
check = True
check_1 = False
print(check)
print(check_1)
#операторы сравнения сопоставяляю два значения и выводят результат в виде булева значения
# оператор операция
# ==          равно
# ===         равно с проверкой типов данных
# !=          отрицание, не равно
# <           меньше
# >           больше
# <=          меньше или равно
# >=          больше или равно
# Булевы операторы
# and     означает и
# or      или
# not     нет

# Таблица истинности для оператора and
# выражение         результат
# True and True    True
# True and False   False
# False and True   False
# False and False  False

# Таблица истинности для оператора or
# выражение           результат
# False or True       True
# True or False       True
# True or True        True
# False or False      False

# Таблица истинности для оператора not унарный оператор
# выражение           результат
# not True            False
# not False           True

print(1 == 1)
print(1 < 1)
print(1 != 3)
print(1 <= 1)
print(True != False)
print(1 == 1.000)
print((4 < 5) and (5 < 6))
print((4 < 5) and (5 > 9))
print((1 == 5) or (2 == 2))
# elif переводится как иначе-если, и содержит блок условий

anna = True
if not True:
    print("hello Anna")
elif not anna:
    print("правда")
elif anna == True:
    print("правда2")
else:
    print("no")

name = "Anna"
number = 13
if name == "Anna" and number != 13:
    print("вы угадали")
else:
    print("вы не угадали")