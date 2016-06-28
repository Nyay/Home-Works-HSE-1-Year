import re

def basic (filename): 
    file = open(filename, 'r', encoding = 'UTF-8') 
    text = file.read()
    text = text.replace('\n',' ')
    text = text.split(' ')
    block = []
    for word in text:
        word = word.strip(',.?!@#$%^&*()[]{}:;\|/')
        word = word.lower()
        block.append(word)
    file.close()
    return block

def reg (block) :
    block2 = []
    for word in block :
        m = re.match('(откро[июя].*|откры(л.*|т(о(го|й|е)|ы(е|х|м(и?)|й)|а(я)?)|в(ать|ш.*)?))', word)
        if m != None :
            if word in block2:
                continue
            else :
                block2.append(word)
    return block2

def final (block2) :
    final = '\n'.join(block2)
    print ('\nНайденные слова:\n' + final)
    
final(reg(basic(input("Введите имя файла: "))))

 
