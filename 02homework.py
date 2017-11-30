a = int(input('a='))
b = int(input('b='))
c = int(input('c='))

x1 = (-b + ((b ** 2 - 4 * a * c) ** 0.5)) / 2
x2 = (-b - ((b ** 2 - 4 * a * c) ** 0.5)) / 2

print(str(x1) + "\n" + str(x2))
