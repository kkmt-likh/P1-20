# Дата: 15.02.22
# Пара: Архитектура компьютерных систем
# Группа: П1-20
# Авторы: Горбунова, Поздняков

# Переводит число из десятичной системы счисления в заданную.
# x [int] - исходное число; base [int] - основание заданной СС
# Возвращает строку - переведенное число
def dec_to_base(x: int, base: int) -> str:
    res = []; is_neg = x < 0
    if is_neg: x = -x
    while x:
        digit = x % base
        if digit >= 10:
            digit = chr(digit + 87)
        res.append(digit)
        x //= base
    res.reverse()
    res = ''.join(list(map(lambda e: str(e), res)))
    return '-' + res if is_neg else res


# Переводит число из некоторой системы счисления в десятичную
# x [str] - исходное число в форме строки; base [int] - основание исходной СС
# Возвращает значение переведенного числа
def base_to_dec(x: str, base: int) -> int:
    res = 0; i = 0; is_neg = '-' in x
    if is_neg: x = x[1:]
    for char in list(x)[::-1]:
        if (char.isalpha()):
            char = ord(char) - 87
        res += int(char) * base ** i
        i += 1
    return -res if is_neg else res


# получаем первое число и сразу проводим конверсию
data_1 = input('First num: ').split(' ')
op_1 = base_to_dec(data_1[0], int(data_1[1]))

# считываем необходимое действие и СС результата
data_res = input('Action and result\'s base: ').split(' ')

if data_res[0] == '<>': # простая конвертация
    print(dec_to_base(op_1, int(data_res[1])))
else: # не конвертация, нужно второе число
    if data_res[0] not in ['+', '-', 'x', '/']: # проверка валидности ввода
        print('Invalid action')
    else:
        # получаем второе число и проводим конверсию
        data_2 = input('Second num: ').split(' ')
        op_2 = base_to_dec(data_2[0], int(data_2[1]))
        
        # совершаем арифметику по заданным действиям и переводим результат
        if data_res[0] == '+':
            print(f'Result: {dec_to_base(op_1 + op_2, int(data_res[1]))}')
        elif data_res[0] == '-':
            print(f'Result: {dec_to_base(op_1 - op_2, int(data_res[1]))}')
        elif data_res[0] == 'x':
            print(f'Result: {dec_to_base(op_1 * op_2, int(data_res[1]))}')
        elif data_res[0] == '/': # деление пока целочисленное (там нюансы с дробями)
            print(f'Result: {dec_to_base(op_1 // op_2, int(data_res[1]))}')
