#Задание-1

# number_list = [1,2,3,4,44,55,66,12,23,34,65,94,25]
# print(number_list)
# result_list = []
# for number in number_list:
#     if (number ** 0.5 - int(number ** 0.5)) == 0:
#         result_list.append(int(number**0.5))
# print(result_list)

#Задание-2

# day = {'01': 'первое', '02': 'второе', '03': 'третье', '04': 'четвертое', '05': 'пятое', '06': 'шестое', '07': 'седьмое',
#        '08': 'восьмое', '09': 'девятое', '10': 'десятое', '11': 'одинадцатое', '12': 'двинадцатое', '13': 'тринадцатое',
#        '14': 'четырнадцатое', '15': 'пятнадцатое', '16': 'шестнадцатое', '17': 'семнадцатое', '18': 'восемнадцатое',
#        '19': 'девятнадцатое', '20': 'двадцатое', '21': 'двадцать первое', '22': 'двадцать второе', '23': 'двадцать третье',
#        '24': 'двадцать четвертое', '25': 'двадцать пятое', '26': 'двадцать шестое', '27': 'двадцать седьмое',
#        '28': 'двадцать восьмое', '29': 'двадцать девятое', '30': 'тридцатое', '31': 'тридцать первое'}
# month = {'01': 'января', '02': 'февраля', '03': 'марта', '04': 'апреля', '05': 'мая', '06': 'июня', '07': 'июля',
#          '08': 'августа', '09': 'сентября', '10': 'октября', '11': 'ноября', '12': 'декабря'}
# data = '02.11.2013'
# data_part = data.split('.')
# print(f'{day[data_part[0]]} {month[data_part[1]]} {data_part[2]} года')

# Задание-3

# from random import randint
# n = randint(1, 10)
# list = []
# for _ in range(n):
#     list.append(randint(-100, 100))
# print(list)

# Задание-4

# from random import randint
# n = randint(5, 30)
# list1 = []
# for _ in range(n):
#     list1.append(randint(1, 100))
# print(list1)
# list2 = []
# list3 = []
# for i, each in enumerate(list1):
#     if i == 0:
#         list3.append(each)
#         list2.append(each)
#     else:
#         if each not in list2:
#              list2.append(each)
#              list3.append(each)
#         else:list3.pop(list3.index(each))
#
# print('Наш список: ', list1, '\nсписок а): ', list2, '\nсписок б): ', list3)
