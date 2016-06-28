import re

def open_file(filename):
    f = open(filename, 'r', encoding = 'UTF-8')
    lines = f.readlines()
    f.close()
    return lines


def create_file(string):
    f = open('Столицы Стран.txt', 'a')
    f.write(string)
    f.close()
            

def find_number(lines):
    x = 0
    while x < len(lines):
        if '>Столица</a>' in lines[x]:
            try:
                res = re.search('<span style="display: none; speak: none;">([^#&;<>]*?)<', lines[x + 1])
                capt = res.group(1) 
            except AttributeError:
                capt = 'Простите, ваша страница не подошла по формату, попробуйте другую...'
            break
        else:
            x += 1
    create_file('Столица вашей страны: ' + capt + '\n')
    print('Ваш файл создан!')

def main():
    find_number(open_file(input('Введите имя файла(с расширением): ')))

main()
