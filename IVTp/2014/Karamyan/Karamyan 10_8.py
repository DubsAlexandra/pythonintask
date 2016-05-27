# Задача 10, Вариант 11
# Напишите программу "Генератор персонажей" для игры. 
# Пользователю должно быть предоставлено 30 пунктов,
# которые можно распределить между четырьмя характеристиками:
# Сила, Здоровье, Мудрость и Ловкость. Надо сделать так,
# чтобы пользователь мог не только брать эти пункты из общего
# "пула", но и возвращать их туда из характеристик, которым он
# решил присвоить другие значения.

# Карамян Н.Г.
# 27.05.2016

POINT = 30 # Константа
ochki = 30 # Переменная, для очков. Изменяет свое значение в процессе назначения пунктов между характеристками
person = {"Сила":"0","Здоровье":"0","Мудрость":"0","Ловкость":"0"} # Характеристики персонажа
points = 0 # Переменная для назначения пунктов
choice = None # Переменная выбора меню

while choice != 0: # Цикл работы, пока не будет нажат "0"
    print ('''
    0 - Выход
    1 - Добавить пункты к характеристике
    2 - Уменьшить пункты характеристики
    3 - Просмотр характеристик
          ''')

    choice = int(input('Пункт: '))
    
    if choice == 1:
        print ('Пожалуйста, введите характеристику для добавления пунктов.')
        print ('Для изменения доступны', len(person), 'характеристики:')
        
        for item in person:
            print ('\t', item)
            
        char = str(input('\n: '))
        char = char.title()
        
        while char not in person:
             print ('Такого нет. Ещё раз: ')
             char = str(input('\n: '))
             char = char.title()
             
        else:
            print ('\nВведите количество пунктов для данной характеристики. У вас', ochki, 'свободных пунктов')
            points = int(input('\n:'))

            # Начисление пунктов и отрицательное значение
            while points > ochki or points < 0: 
                print ('Вы не можете назначить такое количество пунктов')
                print ('Доступно', ochki, 'свободных пунктов')
                points = int(input('\n:'))
        person[char] = points
        print(points, 'пунктов было добавлено к', char)

        # Изменяем количество доступных к начислению пунктов
        ochki -= points
        
    elif choice == 2:
        print ('Пожалуйста, введите имя характеристики для снятия пунктов.')
        print ('Доступно изменение для: ')
        
        for item in person:
            if int(person[item]) > 0: # Не показываем характеристику, если она равна 
                print ('\t', item)
        char = str(input('\n:'))
        char = char.title()
        
        while char not in person:
             print('Такого нет. Ещё раз: ')
             char = str(input('\n:'))
             char = char.title()
        
        else:
            print ('\nВведите количество пунктов для характеристики.')
            print ('Доступно', person[char], 'пунктов:')
            points = int(input('\n:'))
        
            while points > int(person[char]) or points < 0: # Снятие указанного количества пунктов и отрицательное значение
                print ('Невозможно удалить такое количество пунктов.')
                print ('Доступно', person[char], 'пунктов')
                points = int(input('\n:'))
                       
        person[char] = points
        print(points, 'пунктов было удалено')
        ochki += points # Возвращаем освободившиеся пункты в доступные

                       
    elif choice == 3:
        print('\nХарактеристики героя')
        for item in person:
            print(item, '\t -- \t', person[item])
        
    elif choice == 0:
        print('Bye!')
    else:
        print('Такого нет.')

input ('Жмак')
