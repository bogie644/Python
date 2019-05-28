# -*- coding: utf8 -*-


import random
import sys

class Card:
    def __init__(self, name):
        self.name = name
        self.cards = self._set_card()
        self._set_card


    def _set_card(self):
        card = list(set(random.sample(range(1, 91), 15)))
        cards = [card[:5], card[5:10], card[10:]]
        for card_line in cards:
            card_line.sort()
            card_line.insert(random.randint(0, 3), ' ')
            card_line.insert(random.randint(0, 4), ' ')
            card_line.insert(random.randint(0, 5), ' ')
            card_line.insert(random.randint(0, 6), ' ')
        return cards

    def get_card(self):
        print('-' * 5, 'Ваша карточка ' + self.name, '-' * 5)
        for cards_line in self.cards:
            for elem in cards_line:
                print(elem, end='  ')
            print()
        print('-' * 30, end='\n\n\n')

    def searh(self, barrel):
        self.numbers = 0
        for i, n in enumerate(self.cards):
            if barrel in n:
                self.cards[i][n.index(barrel)] = '-'
                self.numbers += 1
                if self.numbers == 15:
                    print('Игрок ' + self.name + ' победил!')
                    sys.exit(1)
                return True
        return False


class Bag:
    def __init__(self):
        self.barrel = self._set_barrel()
    def _set_barrel(self):
        barrels = [x for x in range(1, 91)]
        random.shuffle(barrels)
        for i, j in enumerate(barrels):
            print('*' * 30)
            print('Новый бочонок: ', j)
            print('*' * 30, end='\n\n')
            yield j
class Computer(Card):
    def __init__(self):
        self.cards = self._set_card()
        self._set_card

    def get_card(self):
        print('-' * 5, 'Карточка компьютера', '-' * 5)
        for cards_line in self.cards:
            for elem in cards_line:
                print(elem, end='  ')
            print()
        print('-' * 30)

def game():

    player = Card('Anton')
    comp = Computer()
    bag = Bag()
    while True:
        barrel = next(bag.barrel)
        player.get_card()
        comp.get_card()
        comp.searh(barrel)
        answer = input('Зачеркнуть номер? ' + str(barrel) + ' (y/n)')
        while answer != 'y' and answer != 'n':
            answer = input('Введите y или n')
            continue
        if answer == 'y':
            if player.searh(barrel):
                continue
            else:
                print('Вы проиграли! Номера ', barrel, ' нет в вашей карточке')
                sys.exit(1)
        elif answer == 'n':
            if player.searh(barrel):
                print('Вы проиграли! Номер ', barrel, ' есть в вашей карточке')
                sys.exit(1)
            else:
                continue


game()