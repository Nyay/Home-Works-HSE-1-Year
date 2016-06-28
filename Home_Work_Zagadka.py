import random

def NewDic():
    f = open('dic.csv', 'r', encoding = 'UTF-8')
    x = ()
    y = []
    for line in f:
        line = line.strip('\ufeff\n')
        x = tuple(line.split(';'))
        y.append(x)
    global d
    
    d = dict(y)
    f.close()
    return d

def GameStrc():
    NewDic()
    print('Привет! Давай сыграем в игру?\nСмотри, я загадаю тебе слово, а ты попробуешь отгадать.\nКоличество попыток, равно длине слова.\nТак и быть я буду тебе давать подсказки...\nПисать слова надо так, чтобы заглавных букв не было!')
    x = random.choice(list(d.keys())) #Выбор подсказки.
    attempts = len(d[x])
    print('Посказка\n' + x + '\n')
    y = input('Что это за слово? \n') #Получаем ответ.
    if y == d[x]: # Проверка ответа
        print('Молодец, ты угадал. Приходи за загадками еще...')
    else:
        while attempts != 0:
            print('Попробуйте еще раз! Попыток осталось: ' + str(attempts - 1))
            y = input('Что это за слово?\n') #Получаем ответ.
            if y == d[x]: # Проверка ответа
                print('Молодец, ты угадал. Приходи за загадками еще...')
                break
            else:
                attempts -= 1
    if attempts == 0:
        print ('Простите, вы проиграли. Это слово - ' + d[x])


GameStrc()
