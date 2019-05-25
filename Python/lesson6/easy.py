# -*- coding: utf8 -*-

# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False
    def get_speed(self):
        return self.speed
    def get_color(self):
        return self.color
    def get_name(self):
        return self.name
    def get_is_police(self):
        return self.is_police
    def go(self):
        print('Машина поехала')
    def stop(self):
        print('Машина остановилась')
    def turn_left(self):
        print('Машина повернула налево')
    def turn_right(self):
        print('Машина повернула направо')

class TownCar(Car):
    pass
class SportCar(Car):
    pass
class WorkCar(Car):
    pass
class PoliceCar(Car):
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = True

mazda = TownCar('200', 'красная', '6')
zil = WorkCar('90', 'Зеленая', '310')
ford = PoliceCar('250','Бело-синяя','Mondeo')
print(zil.get_is_police())
print(mazda.get_is_police())
print(ford.get_is_police())



# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

# Я понимаю, что сразу так сделал, в задании-1?