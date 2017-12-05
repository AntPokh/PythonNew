#Составить алгоритм увеличения всех трех, введённых с клавиатуры, переменных на 5,если среди них есть хотя бы две равные.
# В противном случае выдать ответ «равных нет».

number1 = input("Введите первое число :")
number1 = int(number1)
number2 = input("Введите второе число :")
number2 = int(number2)
number3 = input("Введите третье число :")
number3 = int(number3)
if number1 == number2 or number1 == number3 or number2 == number3:
    print(number1 + number2 + number3 + 5)
else:
    print("Равных нет!")
