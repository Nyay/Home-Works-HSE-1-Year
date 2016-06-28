import re

def open_file(filename):
    f = open(filename, 'r', encoding = 'UTF-8')
    words = f.read()
    f.close()
    return words

def create_file(string):
    f = open('Slonomar.txt', 'w', encoding = 'UTF-8')
    f.write(string)
    f.close()
    return f
    
def find_word(words):
    res = re.sub('комар((а(х|м|ми)|у|ов|ом|е|ы|а)|( |,|.|!|\?|:|;|\n|-))',r'слон\1', words)
    res_sec = re.sub('Комар((а(х|м|ми)|у|ов|ом|е|ы|а)|( |,|.|!|\?|:|;|\n|-))',r'Слон\1', res)
    create_file(str(res_sec))
    print('\n' + 'Слова в файле заменены. Новый текст записан в файл Slonomar.txt' + '\n' + 'Всего хорошего!')
    return res
    
def main():
    find_word(open_file(input('Здравствуйте, для начала работы, введите имя файла: ')))
    
    
main()
