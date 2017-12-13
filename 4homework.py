# Дописать калькулятор

import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def run(a, b):
    return a * b

def ex(a, b):
    return a / b

def cos(a, b):
    return math.cos(a + b)

def sin(a, b):
    return math.sin(a + b)

first, second = int(input('a: ')), int(input('b: '))
operation = input('+, -, *, /, cos or sin ?')

first = int(first)
second = int(second)

if operation == '+':
    result = add(first, second)
elif operation == '-':
    result = sub(first, second)
elif operation == '*':
    result = run(first, second)
elif operation == '/':
    result = ex(first, second)
elif operation == 'cos':
    result = cos(first, second)
elif operation == 'sin':
    result = sin(first, second)
else:
    result = None

if result is not None:
    print('Result: ', result)
else:
    print('Wrong operation')


# 1. Написать функцию is_prime(a),
# Которая принимает число и возвращает True или False в зависимости от того,
# простое это число или нет Пример:
# >>is_prime(3)
# >>True
# >>is_prime(4)
# >>False
#
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    else:
        return True


# print(is_prime(2))
# Вывести на экран 10 первых простых чисел используют функцию задания 1
#
i,j = 1,0
while j < 10:
    result = is_prime(i)
    if result:
        print(i, result)
        j = j + 1
    i = i+1

# Написать функцию, которая выводит на экран n первых четных чисел.
# >>func(3):
# >>2, 4, 6
#
def nuber_num(n):
    for i in range(2, (n + 1) * 2, 2):
        print(i)


print(nuber_num(300))


#Написать функцию, которая определяет количество разрядов введенного целого числа.
def task_3(n):
    count = 0
    while n > 1:
        n /= 10
        count += 1
    return count
print(task_3(500))

# Написать функцию, которая определяет количество разрядов введенного целого числа.
# Пример:
# >> func(40)
# >> 2
def func(n):
    i = 0
    while n > 0:
        n = n // 10
        i += 1
    return i


num = abs(int(input('Введите число: ')))
print('Количество разрядов:', func(num))


# Написать функцию принимающую имя фигуры (квадрат, треугольник, ромб), ее размерность и рисует эту фигуру на экран
# Пример:
# >> print_figure(‘треугольник’, 3)
# *
# **
# ***
#
def print_figure(square, n, nm):
    a = n
    b = nm
    for i in range(a):
        print('*' * b)

print(print_figure('*', 4, 8))

def print_figurer(triangle, n):
    a = n
    for i in range(a):
        print(' ' * (a - i), end='')
        print('*' * i, end='')
        print('*' * (i - 1))

print(print_figurer('*', 5))



def print_figure(rhomb, n):
    a = n
    for i in range(a):
        print(' ' * (a - i), end='')
        print('*' * i, end='')
        print('*' * (i - 1))

    for i in range(a):
        print(' ' * (i + 1), end='')
        print('*' * (a - i - 1), end='')
        print('*' * (a - i - 1 - 1))

print(print_figure('*', 8))

# Решить рекурсивно задачу нахождения n-го числа фиббоначи

def fibo(n):
    a = [0, 1]
    for i in range(2, n + 1):
        a.append(a[i-1] + a[i-2])
    print(a)

n = 10
fibo(n)

