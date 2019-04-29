#Задача-1

a = 100
b = 'listen'
c = [1, 3, 10, 'name']
d = (3, 10, 'data', '?')
print(a, b, c)
print(c[3])
print(d[2])
name = input('Введите Ваше имя: ')
print('Здравствуйте, ' + name)

# Задача-2

print(name + ' ,введите число: ', end='')
number = int(input())
print(str(number) + ' + 2 =', number + 2)

# Задача-3

age = int(input('Сколько Вам лет:'))
if age >= 18:
    print('"Доступ разрешен"')
else: print('"Извините, пользование данным ресурсом только с 18 лет"')