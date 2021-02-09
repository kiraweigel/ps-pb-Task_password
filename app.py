password = input('Введите пароль ')


try: 
    result = (len(password)/len(password))
except ZeroDivisionError:
    print('Вы ввели пустой пароль')

try:
    result = (int(password) + 'qwerty')
except TypeError:
    print('Ваш пароль состоит только из цифр')

try:
    result = (int(password)/2)
except ValueError:
    print('Требования к паролю соблюдены')

    