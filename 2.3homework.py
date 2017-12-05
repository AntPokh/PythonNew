# Считать целое число с клавиатуры.
# Если число делится на 5 вывести на экран слово ‘fiz’,
# если число делится на 3 вывести ‘buz’,
# если число делится на 3 и 5 вывести ‘fizbuz’.

number = input("Введите число :")
number = int(number)
if number % 5 == 0:
    print('fiz')
elif number % 3 == 0:
    print('buz')
elif number % 5 == 0 and number % 3 == 0:
    print('fizbuz')
else:
    print("Wrong action!")