#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

import random, string
import sys, codecs
print (sys.stdout.encoding)
print (sys.getdefaultencoding())

#load file
with open('words_ukr.txt', encoding='utf-8') as f:
#with open('words_eng.txt') as f:
#    for i in f:
 #       print i.decode('utf-8')
        #.encode('cp1252', 'replace')
        
    words = set( line.strip() for line in f.readlines() )
    #for i in words:
        #print (i)
        #.encode('utf-8', 'ignore')
#creating dictionary
words = { word : len(word) for word in words if len(word) > 2 }

print ("\nПочинаємо!\n")
# first letter random choice
game = random.choice('абвгґдеєжзиіїйклмнопрстуфхцчшщьюя')
print ('Це перша літера: "' + game + '"')

answer = ''
#main loop
while answer != 'в':
    #asking user for a letter
    answer = input('\nДе додати літеру? початок/кінець/вийти [п/к/в] ')
    print (answer.encode('utf-8').decode('utf-8'))
    if answer == 'к':
        letter = input('\nНапиши літеру: ')
        game += letter
    elif answer == 'п':
        letter = input('\nНапиши літеру: ')
        game = letter + game
    elif answer == 'в':
        print ('Виходимо з гри...')
        break
    else:
        print ('Спробуй ще раз, але правильно')
        continue

    #checking if user completed the word
    if game in words:
        print ('\nПрограш. Ти закінчив слово:', game)
        answer = 'в'
        continue

    #removing non-matсhing words from dictionary
    tempwords = words.copy()
    for word in tempwords:
        index = word.find(game)
        if index == -1:
            del words[word]
    print (len(words))

    #removing plural form
    if len(game) == 2:
        tempwords = words.copy()
        for k in tempwords:
            if (k[-1] == 'S' and  k[:-1] in words) or\
               (k[-3:] == 'IES' and k[:-3]+'Y' in words):
                del words[k]
    
    #creating sorted list with matching words starting with longest
    sorted_words = sorted(words, key=words.get, reverse=True)
    sorted_words = [ word for word in sorted_words if not len(word) % 2  ]\
                       + [ word for word in sorted_words if len(word) % 2  ]

    for i in sorted_words:
        print (i)

    for word in sorted_words:
        index = word.find(game)
        if index != -1:
            ai_word = word
            print ('ai choice now:', ai_word)
            if index == 0:
                game +=  ai_word[len(game)]
            else:
                game = ai_word[index-1] + game

            break
    else:
        print ('немає в словнику такого: ', game)
        break

    if game in words:
        print ('n\Виграш. Я закінчив слово:', game)
        answer = 'Q'
        continue

    print ('Add a letter before or after: "' + game + '"')
