import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    print(f'''Bagels, a deductive logic game. By Al Sweigart al@inventwithpython.com'
I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:'
When I say:\t\tThat means:'
Pico\t\t\tOne digit is correct but in the wrong position.'
Fermi\t\t\tOne digit is correct and in the right position.'
Bagels\t\t\tNo digit is correct.'
For example, if the secret number was 248 and your guess was 843, the 26. clues would be Fermi Pico.''')

    while True:  # Основной цикл игры
        # Переменная в которой хранится секретное число
        secret_num = get_secret_num()  # должен угадать игрок
        print('I have thought up a number')
        print(f'You have {MAX_GUESSES} guesses to get it')

        num_guesses = 1
        while num_guesses <= MAX_GUESSES:
            guess = ''
            # Продолжаем итерации до получения правильной догадки:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f'Guess #{num_guesses}')
                guess = input('> ')

            clues = get_clues(guess, secret_num)
            print(clues)
            num_guesses += 1

            if guess == secret_num:
                break  # Правильно выходим из цикла
            if num_guesses > MAX_GUESSES:
                print(f'You run out of guesses!')
                print(f'The answer was {secret_num}')

        # Спрашиваем игрока хочет ли он сыграть еще раз.
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')


def get_secret_num():
    """Возвращает строку из NUM_DIGITS уникальных случайных цифр"""
    numbers = list('0123456789')  # Создает список цифр от 0 до 9
    random.shuffle(numbers)  # Перетасовываем их случайным образом

    # Берем первые NUM_DIGITS цифр списка для нашего секретного числа:
    secret_num = ''
    for i in range(NUM_DIGITS):
        secret_num += str(numbers[i])
    return secret_num


def get_clues(guess, secret_num):
    """Возвращает строку с подсказками pico, fermi и bagels
     для полученной на входе пары из догадки и секретного числа."""
    if guess == secret_num:
        return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            #  Правильная цифра на правильном месте
            clues.append('Fermi')
        elif guess[i] in secret_num:
            # Правильная цифра на неправильном месте
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'  # Правильных цифр нет вообще
    else:
        # Сортируем подсказки в исходном порядке, чтобы их исходный порядок ничего не выдавал.
        clues.sort()
        # Склеиваем список подсказок в одно строковое значение
        return ' '.join(clues)


# Если программа не импортируется, а запускается, производим запуск
if __name__ == '__main__':
    main()
