# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота. Достаточно сделать так, чтобы бот не брал конфет больше положенного или больше чем имеется в куче.
# b) Подумайте как наделить бота ""интеллектом"". Напоминаю, если перед пользователем будет лежать 29 конфет, то он, однозначно, проиграет. Достаточно довести игру до такой ситуации.

import random

# Защита от дурака для чисел
def foolproof(num):
    if num.isdigit() and 1 <= int(num) <= 28:
        return True
    else:
        return False

# Защита от дурака для ответов
def answer(string):
    if string.lower() == 'да' or string.lower() == 'нет':
        return True
    else:
        return False


# Выбор противника
def enemy(string):
    if string.lower() == 'друг' or string.lower() == 'бот' or string.lower() == 'я на диете':
        return True
    else:
        return False


# Жеребьевка
def draw():
    num = random.randint(0, 2)
    if num == 0:
        return False
    else:
        return True


# Интеллект бота
def intellect_bot(remains, flag_bot):
    if flag_bot == False:
        return random.randint(1, 29)
    else:
        if remains <= 28:
            return remains
        elif 29 < remains < 58:
            return remains - 29
        elif 57 < remains < 87:
            return remains - 58
        else:
            return random.randint(1, 29)


# Подписи
def Signature():
    print(
        "\n________________________\nthe program was implemented by: \n                     Dmitry Pyanzin\n                     Danila Obgerin\n                     Nikita Muratikov")
    print(
        "                     Valeriya Shevchuk\n                     Nadegda lisova\n                     Ivan Savkin\n                     Aziz Sharakhmedov\n________________________\n")


# Вводимые переменные
total = 121
thoughts_of_bot = ['Скайнет победит!', 'Вам конец - кожаные ублюдки!',
                   'За миллионы лет эволюции чудес не произошло, ты все равно тупая обезьяна',
                   'Ты проиграешь, мешок с костями', 'Ты уже давно батарейка и живешь ты в матрице!']
flag = True
flag_motion = None
flag_bot = None
flag_ans = True

# Основная программа
print('\nДобро пожаловать в игру, "КОМУ ДОСТАНУТСЯ ВСЕ КОНФЕТКИ?"\n')
print('Хочешь поиграть? Ответить нужно "ДА" или "НЕТ" \n')

while True:
    ans = input()
    if answer(ans) == False:
        print('\nОтвет должен быть "ДА" или "НЕТ"! \n')
    else:
        if ans.lower() == 'нет':
            print('\nНу не хочешь, как хочешь! Пока! Пока!')
            Signature()
            exit()
        else:
            print("                                                                     ПРАВИЛА ИГРЫ")
            print(
                '\nВ корзине лежит 2021 конфета! Ты и твой противник по очереди берут конфеты из корзины. Взять можно от 1 до 28 конфет. Ход пропускать нельзя! Кто ходит первый, определяется случайным образом!\n')
            print(
                'Играть можно как против компьютера, так и против друга. Тот, кто последним ходом забирает оставшиеся конфеты, тот и победил. Ему достаются все 2021 конфета и кариес!\n')
            input('Если с правилами игры ознакомился, то нажми Enter\n')
            print('Теперь тебе нужно выбрать противника!\n')
            while True:
                ans = input(
                    'Напиши "ДРУГ", чтобы играть против друга или "БОТ", чтобы играть против компьютера! Для выхода из игры введите "Я НА ДИЕТЕ"!. \n')
                if enemy(ans) == False:
                    print("\nНажимай на клавиши внимательнее!\n")
                else:
                    flag_motion = draw()
                    if ans.lower() == 'я на диете':
                        print("\nИспугался, так и скажи!")
                        Signature()
                        exit()
                    elif ans.lower() == 'друг':
                        while flag:
                            if flag_motion == True:
                                print("\nТвой ход:\n")
                            else:
                                print("\nХод твоего друга:\n")
                            print(f'Конфет в корзине {total}\n')
                            number = input('Введи число от 1 до 28\n')
                            if foolproof(number) == False:
                                print("\nА может быть все таки число от 1 до 28?")
                            else:
                                print(f'\nИз корзины забрали {number} конфет(-у)')
                                total -= int(number)
                                if flag_motion == True and total <= 0:
                                    print('\nТы победил и забираешь все конфеты!\n')
                                    flag = False
                                elif flag_motion == False and total <= 0:
                                    print('\nПобедил твой друг и он забирает все конфеты!\n')
                                    flag = False
                                flag_motion = not flag_motion
                    else:
                        while flag_ans:
                            ans = input('Хочешь сыграть против умного бота?. Напиши "ДА" или "НЕТ" \n')
                            if answer(ans) == False:
                                print('\nОтвет должен быть "ДА" или "НЕТ"! \n')
                            else:
                                if ans.lower() == 'да':
                                    flag_bot = True
                                    flag_ans = False
                                else:
                                    flag_bot = False
                                    flag_ans = False
                        while flag:
                            if flag_motion == True:
                                print("\nТвой ход!\n")
                                print(f'Конфет в корзине {total}\n')
                                number = input('Введи число от 1 до 28\n')
                                if foolproof(number) == False:
                                    print("\nА может быть все таки число от 1 до 28?")
                                else:
                                    print(f'\nИз корзины забрали {number} конфет(-у)')
                                    total -= int(number)
                                    if total <= 0:
                                        print('\nТы победил и забираешь все конфеты!\n')
                                        flag = False
                                    flag_motion = not flag_motion
                            else:
                                print("\nХод БОТА!\n")
                                print(f'Конфет в корзине {total}\n')
                                num = intellect_bot(total, flag_bot)
                                print(f'Из корзины забрали {num} конфет(-у)\n')
                                print(thoughts_of_bot[random.randint(0, 4)])
                                input('\nНажми Enter')
                                total -= num
                                if total <= 0:
                                    print('\nЯ выиграл - Кожаный ублюдок и забираю все эти сладенькие конфетки себе!\n')
                                    flag = False
                                flag_motion = not flag_motion
                print('Спасибо за игру!\n')
                print('Хочешь еще поиграть? Напечатай "ДА" или "НЕТ"')
                while True:
                    ans = input()
                    if answer(ans) == False:
                        print('\nОтвет должен быть "ДА" или "НЕТ"! \n')
                    else:
                        if ans.lower() == 'нет':
                            print('\nСпасибо за игру! Ждем тебя снова!')
                            Signature()
                            exit()
                        else:
                            flag = True
                            flag_ans = True
                            total = 121
                            break