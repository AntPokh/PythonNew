#1. Составить программу, которая требует ввести два числа.
# Если первое число больше второго, то программа печатает слово больше.
# Если первое число меньше второго, то программа печатает слово меньше.
# А если числа равны, программа напечатает сообщение Эти числа равны.

print("> or <")

number1 = input("Введите первое число :")
number1 = int(number1)
number2 = input("Введите второе число :")
number2 = int(number2)

if number1 > number2:
    print(number1)
elif number1 < number2:
    print(number1)
elif number1 == number2:
    print("Эти числа равны")
else:
    print("Wrong action!")