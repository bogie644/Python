form = {'name': input('Введите Ваше имя: '), 'surname': input('Введите Вашу фамилию: '), 'age': input('Введите Ваш возраст: '), 'weight': input('Введите Ваш вес: ')}
if int(form['age']) < 10:
    print(form['name'], form['surname'], form['age'] + ' лет', 'Вы еще очень молоды!')

elif (int(form['age']) >= 10 and int(form['age']) <=30):
    if int(form['weight']) < 20:
        print(form['name'], form['surname'], form['age'] + ' лет ', 'вес ' + form['weight'], 'Вы живой?')
    elif int(form['weight']) >= 20 and int(form['weight']) < 50:
        print(form['name'], form['surname'], form['age'] + ' лет ', 'вес ' + form['weight'], '- хорошее состояние')
    elif int(form['weight']) >= 50 and int(form['weight']) <= 90:
        print(form['name'], form['surname'], form['age'] + ' лет ', 'вес ' + form['weight'], '- следует заняться собой')
    elif int(form['weight']) > 90 and int(form['weight']) <= 120:
        print(form['name'], form['surname'], form['age'] + ' лет ', 'вес ' + form['weight'], '- следует обратиться к врачу')
    elif int(form['weight']) > 120:
        print(form['name'], form['surname'], form['age'] + ' лет ','вес ' + form['weight'], 'Так бывает?')

elif int(form['age']) > 30 and int(form['age']) <= 50:
    if int(form['weight']) < 20:
        print(form['name'], form['surname'], form['age'] + ' год ', 'вес ' + form['weight'], 'Вы живой?')
    elif int(form['weight']) >= 20 and int(form['weight']) < 50:
        print(form['name'], form['surname'], form['age'] + ' лет ', 'вес ' + form['weight'], '- хорошее состояние')
    elif int(form['weight']) >= 50 and int(form['weight']) <= 90:
        print(form['name'], form['surname'], form['age'] + ' лет ', 'вес ' + form['weight'], '- следует заняться собой')
    elif int(form['weight']) > 90 and int(form['weight']) <= 120:
        print(form['name'], form['surname'], form['age'] + ' лет ', 'вес ' + form['weight'], '- следует обратиться к врачу')
    elif int(form['weight']) > 120:
        print(form['name'], form['surname'], form['age'] + ' год ', 'вес ' + form['weight'], 'Так бывает?')


elif int(form['age']) > 50 and int(form['age']) <= 70:
    if int(form['weight']) < 20:
         print(form['name'], form['surname'], form['age'] + ' год ', 'вес ' + form['weight'], 'Вы живой?')
    elif int(form['weight']) >= 20 and int(form['weight']) < 50:
         print(form['name'], form['surname'], form['age'] + ' лет ', 'вес ' + form['weight'], '- хорошее состояние')
    elif int(form['weight']) >= 50 and int(form['weight']) <= 90:
         print(form['name'], form['surname'], form['age'] + ' лет ', 'вес ' + form['weight'], '- следует заняться собой')
    elif int(form['weight']) > 90 and int(form['weight']) <= 120:
         print(form['name'], form['surname'], form['age'] + ' лет ', 'вес ' + form['weight'], '- следует обратиться к врачу')
    elif int(form['weight']) > 120:
         print(form['name'], form['surname'], form['age'] + ' год ', 'вес ' + form['weight'], 'Так бывает?')

elif int(form['age']) > 70 and int(form['age']) <= 110:
    if int(form['weight']) < 20:
        print(form['name'], form['surname'], form['age'] + ' год ', 'вес ' + form['weight'], 'Вы живой?')
    elif int(form['weight']) >= 20 and int(form['weight']) < 50:
        print(form['name'], form['surname'], form['age'] + ' лет ', 'вес ' + form['weight'], '- хорошее состояние')
    elif int(form['weight']) >= 50 and int(form['weight']) <= 90:
        print(form['name'], form['surname'], form['age'] + ' лет ', 'вес ' + form['weight'], '- следует заняться собой')
    elif int(form['weight']) > 90 and int(form['weight']) <= 120:
        print(form['name'], form['surname'], form['age'] + ' лет ', 'вес ' + form['weight'], '- следует обратиться к врачу')
    elif int(form['weight']) > 120:
        print(form['name'], form['surname'], form['age'] + ' год ', 'вес ' + form['weight'], 'Так бывает?')
else:
    print('Столько не живут!')