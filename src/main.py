from converter import NumConverter
from functions import ALPHABET


def run_check(in_ss):
    if in_ss == 16:
        in_num = input('Введите число для перевода СС: ')
        try:
            for i in str(in_num):
                if str(i) not in ALPHABET:
                    raise Exception
        except Exception:
            print('Ошибка ввода. Значение каждого разряда '
                  'числа должно быть меньше значения СС. '
                  'Буквы должны быть в верхнем регистре.')
            return False
        return in_num
    else:
        try:
            in_num = int(input('Введите число для перевода СС: '))
            if in_num < 0:
                raise Exception
            for i in str(in_num):
                if int(i) >= int(in_ss):
                    raise Exception
            return str(in_num)
        except Exception:
            print('Ошибка ввода. Число должно быть: целое, больше 0, '
                  'значение каждого разряда числа должно быть '
                  'меньше значения СС.')
            return False


def menu():
    """
    Главное меню программы.
    """
    choise = -1
    while choise != 0:
        print(
            '\n'
            'Системы счисления (СС).\n'
            '1. Перевода числа из 2-ной СС в 10-ную СС.\n'
            '2. Перевода числа из 10-ной СС в 2-ную СС.\n'
            '3. Перевода числа из 2-ной СС в 8-ную СС.\n'
            '4. Перевода числа из 8-ной СС в 2-ную СС.\n'
            '5. Перевода числа из 8-ной СС в 16-ную СС.\n'
            '6. Перевода числа из 16-ной СС в 8-ную СС.\n'
            '0. Выход.'
        )

        # Ловим ошибку при вводе некорректных данных
        try:
            choise = int(input('Введите номер меню: '))
        except Exception:
            print('\nНеобходимо ввести целое число от 0 до 6.')
            continue

        if choise == 1:
            in_num = run_check(2)
            if in_num:
                convert = NumConverter(
                    in_ss='2',
                    out_ss='10',
                    in_number=in_num
                )
                print(convert)
        elif choise == 2:
            in_num = run_check(10)
            if in_num:
                convert = NumConverter(
                    in_ss='10',
                    out_ss='2',
                    in_number=in_num
                )
                print(convert)
        elif choise == 3:
            in_num = run_check(2)
            if in_num:
                convert = NumConverter(
                    in_ss='2',
                    out_ss='8',
                    in_number=in_num
                )
                print(convert)
        elif choise == 4:
            in_num = run_check(8)
            if in_num:
                convert = NumConverter(
                    in_ss='8',
                    out_ss='2',
                    in_number=in_num
                )
                print(convert)
        elif choise == 5:
            in_num = run_check(8)
            if in_num:
                convert = NumConverter(
                    in_ss='8',
                    out_ss='16',
                    in_number=in_num
                )
                print(convert)
        elif choise == 6:
            in_num = run_check(16)
            if in_num:
                convert = NumConverter(
                    in_ss='16',
                    out_ss='8',
                    in_number=in_num
                )
                print(convert)
        elif choise == 0:
            print('\nДо скорой встречи!')
        else:
            print('\nНе верная команда. Введите число от 0 до 6.')


if __name__ == '__main__':
    menu()
