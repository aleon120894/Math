import math
# Пользователь вводит два числа. Найдите сумму и произведение данных чисел.

number_one = input("Type 1st number")
number_two = input("Type 2st number")

def plus_other(a, b):

    a = int(a)
    b = int(b)
    c = a + b
    d = a * b

    print(c, d)

plus_other(number_one, number_two)

# Пользователь вводит число. Выведите на экран квадрат этого числа, куб этого числа.

number = input("enter number")

def sqr_cube(n):

    n = int(n)
    sqr = n ** 2
    cube = n ** 3
    print(sqr, cube)

sqr_cube(number)

# Пользователь вводит три числа. Увеличьте первое число в два раза, второе числа уменьшите на 3, третье число возведите в квадрат и затем найдите сумму новых трех чисел.


def mlt_add_sqr(a, b, c):
    int(a)
    float(b)
    int(c)

    first_result = a * 2
    second_result = b - 3
    third_result = c ** 2
    sum = first_result + second_result + third_result

    print(first_result, second_result, third_result, sum)



# Пользователь вводит три числа. Найдите среднее арифметическое этих чисел, а также разность удвоенной суммы первого и третьего чисел и утроенного второго числа.

first = int(input("Enter first number: "))
second = int(input("Type second number: "))
third = int(input("Type third number: "))

def average (a, b, c):

    result = (a + b + c) / 3
    return result

def difference(a, b, c):

    result = 2 * (a + c) - 3 * b
    return result

average_result = average(first, second, third)
difference_result = difference(first, second, third)

print(average_result)
print(difference_result)






# Пользователь вводит сторону квадрата. Найдите периметр и площадь квадрата.

def sqr(side):
    result = side ** 2
    return result


# Пользователь вводит цены 1 кг конфет и 1 кг печенья. Найдите стоимость: а) одной покупки из 300 г конфет и 400 г печенья; б) трех покупок, каждая из 2 кг печенья и 1 кг 800 г конфет.
a = float(input("Price for 1 kilogram of sweets: "))
b = float(input("Weight (in kg): "))
c = float(input("Price for one kilogram of cookies: "))
d = float(input("Weight (kilogram): "))

def marketing_operations(a, b, c, d):
    x = (a / 1000) * c
    y = (b / 1000) * d
    z = x + y

    print ("Price ",c,"kilogram of cookies: ",x," dollars")
    print ("Price ",d,"kilogram of cookies: ",y," dollars")
    print ("Purchase price: ",z," Dollars")



# Пользователь вводит время в минутах и расстояние в километрах. Найдите скорость в м/c.

def speed(time, distance):

    sp = distance / time
    return sp



# Даны катеты прямоугольного треугольника. Найдите площадь, периметр и гипотенузу треугольника.

def triangle(first_cat, second_cat):
    hypotenuse = math.sqrt((first_cat ** 2) + (second_cat ** 2))
    perimeter = first_cat + second_cat + hypotenuse
    area = first_cat * second_cat / 2

    return hypotenuse, perimeter, area



# Дано значение температуры в градусах Цельсия. Вывести температуру в градусах Фаренгейта.

def set_temperature(cl):

    far = cl * 1.8 + 32
    return far