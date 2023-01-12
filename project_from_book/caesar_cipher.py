
def caesar_cipher(message: str, key: int, mode: str = 'encrypt' or 'decrypt') -> str:
    """Шифр Цезаря
    Шифр Цезаря — шифр сдвига, в котором шифрование и дешифровка букв
    производятся путем сложения и вычитания соответствующих чисел.
    Дополнительная информация: https://ru.wikipedia.org/wiki/Шифр_Цезаря
    Теги: короткая, для начинающих, криптография, математическая"""

    from string import ascii_uppercase
    if 0 > key > len(ascii_uppercase)-1:
        return 'N/A'

    # Для хранения зашифрованного/расшифрованного варианта сообщения:
    translated = ''

    # Зашифровываем/расшифровываем каждый символ сообщения:
    for symbol in message.upper():
        if symbol in ascii_uppercase:
            # Получаем зашифрованное (расшифрованное) числовое значение для символа.
            num = ascii_uppercase.find(symbol)
            if mode == 'encrypt':
                num += key
            elif mode == 'decrypt':
                num -= key
            # Производим переход по кругу, если число больше длины ascii_uppercase или меньше 0:
            if num >= len(ascii_uppercase):
                num -= len(ascii_uppercase)
            elif num < 0:
                num += len(ascii_uppercase)
            # Добавляем соответствующий числу зашифрованный/расшифрованный символ в translated:
            translated += ascii_uppercase[num]
        else:
            # Просто добавляем символ без шифрования/расшифровки:
            translated += symbol

    # Выводим зашифрованную/расшифрованную строку на экран:
    return translated


print(caesar_cipher(message='Meet me by the rose bushes tonighlt.', key=4, mode='encrypt'))
print(caesar_cipher(message='QIIX QI FC XLI VSWI FYWLIW XSRMKLX', key=4, mode='decrypt'))

