# Задача-1

number = int(input('Введите число: '))
while number <= 0 or number >= 10:
    number = int(input('Вы ввели неверное число! Введите число в диапозоне от 1 до 9: '))
print('Ваше число возведенное во 2ю степень = ', number ** 2)

# Задача-2

a = int(input('Введите переменную а:'))
print('a = ', a)
b = int(input('Введите переменную b:'))
print('b = ', b)
a = a + b
b = a - b
a = a - b
print('Теперь a = ', a, 'b = ', b)