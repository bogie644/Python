# -*- coding: utf8 -*-
# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.


class Person:
    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor
    def get_health(self):
        return self.health
    def get_damage(self):
        return self.damage
    def get_armor(self):
        return self.armor
    def _calculate_damage(self, enemy):
        return self.get_damage() / enemy.get_armor()
    def attack(self):
        damage = self._calculate_damage(self)
        self.health = self.get_health() - damage

class Player(Person):
    pass

class Enemy(Person):
    pass

class Game:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
    def start(self):
        last_attacker = self.player
        while self.player.get_health() > 0 and self.enemy.get_health() > 0:
            if last_attacker == player:
                self.enemy.attack()
                last_attacker = self.enemy
            else:
                self.player.attack()
                last_attacker = self.player
        if self.player.get_health() > 0:
            print('Игрок победил!')
        else:
            print('Враг победил!')

player = Player('Anton', 100, 10, 1.2)
enemy = Enemy('Vova', 100, 15, 0.7)
game = Game (player, enemy)
game.start()

