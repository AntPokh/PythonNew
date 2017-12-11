# 3. Вывести таблицу умножения на экран.
print("Таблица умножения")

for i in range(1, 10):
    for x in range(1, 10):
        if x == 0:
            continue
        print(f'{i} * {x} = {i * (x)}')
    print()

# 4. Вывести на экран фигуры со звездочек (
# Ромб, Елочка, Треугольник, Квадрат, ступеньки

# Ромб

a = 6

for i in range(a):
    print(' ' * (a - i ), end = '')
    print('*' * i, end = '')
    print('*' * (i-1))

for i in range(a):
    print(' ' * (i + 1), end = '')
    print('*' * (a - i - 1), end = '')
    print('*' * (a - i - 1 - 1))

#Ёлка
a = 6

b = 3

for j in range(b):
    for i in range(a):
        print(' ' * (a-i), end='')
        print('*' * i, end='')
        print('*' * (i-1))

print()
print()
print()

#треугольник
for i in range(a):
     print(' ' * (a-i), end='')
     print('*' * i, end='')
     print('*' * (i-1))

print()

# Квадрат
a = 4

b = 8

for i in range(a):
     print('*' * b)

print()

# Ступеньки ???



# Напишите программу, запрашивающую имя, фамилия, отчество и номер группы студента и выводящую введённые данные

TITLE = 'Лабораторная работа №1'

name = input('ФИО: ')
group = 'Выполнил(а): ст. гр.: ' + input('Group: ')

len_tittle = len(TITLE)
len_name = len(name)
len_group = len(group)

if len_tittle > len_name and len_tittle > len_group:
    max_len = len_tittle
elif len_name > len_tittle and len_name > len_group:
    max_len = len_name
else:
    max_len = len_group

print('*' * (max_len + 4))
print('* ' + TITLE + ' ' * (max_len - len_tittle) + ' *')
print('* ' +  group + ' ' * (max_len - len_group) + ' *')
print('* ' + name + ' ' * (max_len - len_name) + ' *')
print('*' * (max_len + 4))