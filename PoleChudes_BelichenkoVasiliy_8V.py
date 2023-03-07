letter = []
end = 0
count = 0
print('Добро пожаловать в ежегодную игру "Поле Чудес"!!!')
print("Правила игры:")      #Правила игры
print("Будет загаданно слово, вы можете его отгадывать по буквам, или можете вввести всё слово сразу")
print("Для слова выведеться его определение")
print("В любой момент игры вы можете ввести !help для просмотра правил")
print("Команда !letters же показывает все использованные вами буквы")
print("Пожалуйста, для продолжения игры введите число от 1 до 3!")
a = input()
while a != "1" and a != "2" and a != "3":     #Выборка слова
    print("Некоректный ввод! Пожалуйста, введите число от 1 до 3!")
    a = input()
if a == "1":
    word = "л и т е р а т у р о в е д"
    print("Итак, слово было выбранно!")
    tword = "_ * @ $ % & @ # % ? = $ 0"
    print(tword)
    print('"Человек, професионально занимающийся литературоведением"')
    print('"ENTER для продожения"')
    input()
    print()
    print("Выберете букву, которую вы хотите открыть:")
    while True:
        a = str(input())
        if list(a) == word.split(" "):
            end = 1
            count = count + 1
            break
        if a == "!help":     #!help
            print("Было загаданно слово")
            print(tword)
            print('"Человек, професионально занимающийся литературоведением"')
            print("Вы можете его отгадывать по буквам, или можете вввести всё слово сразу")
            print("В любой момент игры вы можете ввести !help для очередного просмотра правил")
            print("Команда !letters же показывает все использованные вами буквы")
            print("Выберете букву, которую вы хотите открыть:")
        elif a == "!letters":
            if len(letter) == 0:
                print("Вы не ввели ни одной буквы")
                print("Выберете букву, которую вы хотите открыть:")
            else:
                print(*letter, sep='\t')
                print()
                print("Выберете букву, которую вы хотите открыть:")
        elif a.isdigit():
            print("Вас просили ввести букву, а не число!")
        elif a.isalpha():
            if len(a) == 1 and a not in letter:
                if a.lower() in word:
                    print("Откройте букву!")
                    if a.lower() == "л":     #Замена букв в слове
                        tword = tword.replace('_', 'л')
                        letter.append(a)
                    elif a.lower() == "и":
                        tword = tword.replace('*', 'и')
                        letter.append(a)
                    elif a.lower() == "т":
                        tword = tword.replace('@', 'т')
                        letter.append(a)
                    elif a.lower() == "е":
                        tword = tword.replace('$', 'е')
                        letter.append(a)
                    elif a.lower() == "р":
                        tword = tword.replace('%', 'р')
                        letter.append(a)
                    elif a.lower() == "а":
                        tword = tword.replace('&', 'а')
                        letter.append(a)
                    elif a.lower() == "у":
                        tword = tword.replace('#', 'у')
                        letter.append(a)
                    elif a.lower() == "о":
                        tword = tword.replace('?', 'о')
                        letter.append(a)
                    elif a.lower() == "в":
                        tword = tword.replace('=', 'в')
                        letter.append(a)
                    elif a.lower() == "д":
                        tword = tword.replace('0', 'д')
                        letter.append(a)
                    print(tword)
                    if tword == word:
                        end = 1
                        break
                else:
                    print("Вашей буквы нет в слове!")
                    letter.append(a)
                    print(tword)
            elif len(a) == 1 and a in letter:
                print("Вы уже говорили эту букву!")
                print(tword)
            elif a == word:
                end = 1
                break
            else:
                print("Ваше слово не подходит!")
        else:
            print("В слове не может быть цыфр!")
        count = count + 1
    if end == 1:    #Победа
        print("И ВЫ ПОБЕДИЛИ В НАШЕМ КОНКУРСЕ!!!")
        print("Вы угадали слово с", count, "попытки/ок")
        print('Загаданным словом был "ЛИТЕРАТУРОВЕД"')
        print("Спасибо за участие! До свидания!")
elif a == "2":
    word = "х и т и н"
    print("Итак, слово было выбранно!")
    tword = "_ * @ * %"
    print(tword)
    print('"Кожный покров всех членистоногих"')
    print('"ENTER для продожения"')
    input()
    print()
    print("Выберете букву, которую вы хотите открыть:")
    while True:
        a = str(input())
        if list(a) == word.split(" "):
            end = 1
            count = count + 1
            break
        if a == "!help":      #!help
            print("Было загаданно слово")
            print(tword)
            print('"Кожный покров всех членистоногих"')
            print("Вы можете его отгадывать по буквам, или можете вввести всё слово сразу")
            print("В любой момент игры вы можете ввести !help для очередного просмотра правил")
            print("Команда !letters же показывает все использованные вами буквы")
            print("Выберете букву, которую вы хотите открыть:")
        elif a == "!letters":
            if len(letter) == 0:
                print("Вы не ввели ни одной буквы")
                print("Выберете букву, которую вы хотите открыть:")
            else:
                print(*letter, sep='\t')
                print()
                print("Выберете букву, которую вы хотите открыть:")
        elif a.isdigit():
            print("Вас просили ввести букву, а не число!")
        elif a.isalpha():
            if len(a) == 1 and a not in letter:
                if a.lower() in word:
                    print("Откройте букву!")
                    if a.lower() == "х":     #Замена букв в слове
                        tword = tword.replace('_', 'х')
                        letter.append(a)
                    elif a.lower() == "и":
                        tword = tword.replace('*', 'и')
                        letter.append(a)
                    elif a.lower() == "т":
                        tword = tword.replace('@', 'т')
                        letter.append(a)
                    elif a.lower() == "н":
                        tword = tword.replace('%', 'н')
                        letter.append(a)
                    print(tword)
                    if tword == word:
                        end = 1
                        break
                else:
                    print("Вашей буквы нет в слове!")
                    letter.append(a)
                    print(tword)
            elif len(a) == 1 and a in letter:
                print("Вы уже говорили эту букву!")
                print(tword)
            elif a == word:
                end = 1
                break
            else:
                print("Ваше слово не подходит!")
        else:
            print("В слове не может быть цыфр!")
        count = count + 1
    if end == 1:
        print("И ВЫ ПОБЕДИЛИ В НАШЕМ КОНКУРСЕ!!!")     #Победа
        print("Вы угадали слово с", count, "попытки/ок")
        print('Загаданным словом был "ХИТИН"')
        print("Спасибо за участие! До свидания!")
elif a == "3":
    word = "п р о т о н"
    print("Итак, слово было выбранно!")
    tword = "_ * @ $ @ %"
    print(tword)
    print('"Мельчайшая положительно-заряженная частица ядра атома"')
    print('"ENTER для продожения"')
    input()
    print()
    print("Выберете букву, которую вы хотите открыть:")
    while True:
        a = str(input())
        if list(a) == word.split(" "):
            end = 1
            count = count + 1
            break
        if a == "!help":      #!help
            print("Было загаданно слово")
            print(tword)
            print('"Мельчайшая положительно-заряженная частица ядра атома"')
            print("Вы можете его отгадывать по буквам, или можете вввести всё слово сразу")
            print("В любой момент игры вы можете ввести !help для очередного просмотра правил")
            print("Команда !letters же показывает все использованные вами буквы")
            print("Выберете букву, которую вы хотите открыть:")
        elif a == "!letters":
            if len(letter) == 0:
                print("Вы не ввели ни одной буквы")
                print("Выберете букву, которую вы хотите открыть:")
            else:
                print(*letter, sep='\t')
                print()
                print("Выберете букву, которую вы хотите открыть:")
        elif a.isdigit():
            print("Вас просили ввести букву, а не число!")
        elif a.isalpha():
            if len(a) == 1 and a not in letter:
                if a.lower() in word:
                    print("Откройте букву!")
                    if a.lower() == "п":     #Замена букв в слове
                        tword = tword.replace('_', 'п')
                        letter.append(a)
                    elif a.lower() == "р":
                        tword = tword.replace('*', 'р')
                        letter.append(a)
                    elif a.lower() == "о":
                        tword = tword.replace('@', 'о')
                        letter.append(a)
                    elif a.lower() == "т":
                        tword = tword.replace('$', 'т')
                        letter.append(a)
                    elif a.lower() == "н":
                        tword = tword.replace('%', 'н')
                        letter.append(a)
                    print(tword)
                    if tword == word:
                        end = 1
                        break
                else:
                    print("Вашей буквы нет в слове!")
                    letter.append(a)
                    print(tword)
            elif len(a) == 1 and a in letter:
                print("Вы уже говорили эту букву!")
                print(tword)
            elif a == word:
                end = 1
                break
            else:
                print("Ваше слово не подходит!")
        else:
            print("В слове не может быть цыфр!")
        count = count + 1
    if end == 1:
        print("И ВЫ ПОБЕДИЛИ В НАШЕМ КОНКУРСЕ!!!")      #Победа
        print("Вы угадали слово с", count, "попытки/ок")
        print('Загаданным словом был "ПРОТОН"')
        print("Спасибо за участие! До свидания!")
input()