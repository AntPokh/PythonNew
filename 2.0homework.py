#0. Написать программу калькулятор (которая спрашивает у пользователя два числа, операцию (+,-,/,*, **, sin, cos,) и выводит на экран результат.

print("Basic calculator")

number1 = input("Введите первое число :")
number1 = int(number1)
number2 = input("Введите второе число :")
number2 = int(number2)
action = input("Выберите действие: +,-,/,*, **, sin, cos :")
import math

if action == "+":
    print(number1 + number2)
elif action == "-":
    print(number1 - number2)
elif action == "/":
    print(number1 / number2)
elif action == "*":
    print(number1 * number2)
elif action == "**":
    print(number1 ** number2)
elif action == "sin":
    print(math.sin(number1 + number2))
elif action == "cos":
    print(math.cos(number1 + number2))
else:
    print("Wrong action!")

