import random
import string

#load file
#with open('words_ukr.txt') as f:
with open('words_eng.txt') as f:
    words = set( line.strip() for line in f.readlines() )
#creating dictionary
words = { word.upper() : len(word) for word in words if len(word) > 2 }

print "\nLet's start the fight!\n"
# first letter random choice
game = random.choice(string.uppercase)
print 'The first letter is "' + game + '"'

answer = ''
#main loop
while answer != 'Q':
    #asking user for a letter
    answer = raw_input('\nwhere do you want to add a letter? start/end/quit [s/e/q] ').upper()
    if answer == 'E':
        letter = raw_input('\nPlease provide a letter: ').upper()
        game += letter
    elif answer == 'S':
        letter = raw_input('\nPlease provide a letter: ').upper()
        game = letter + game
    elif answer == 'Q':
        print 'quitting the game...'
        break
    else:
        print 'not valid input, try once again'
        continue

    #checking if user completed the word
    if game in words:
        print '\nYou lost! you completed the word:', game
        answer = 'Q'
        continue

    #removing non-mathing words from dictionary
    tempwords = words.copy()
    for word in tempwords:
        index = word.find(game)
        if index == -1:
            del words[word]
    print len(words)

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
        print i

    for word in sorted_words:
        index = word.find(game)
        if index != -1:
            ai_word = word
            print 'ai choice now:', ai_word
            if index == 0:
                game +=  ai_word[len(game)]
            else:
                game = ai_word[index-1] + game

            break
    else:
        print 'no such word in my dictionary', game
        break

    if game in words:
        print '\nYou win! I completed the word:', game
        answer = 'Q'
        continue

    print 'Add a letter before or after: "' + game + '"'
