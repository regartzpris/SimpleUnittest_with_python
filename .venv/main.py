import random


def do(num=0):
    try:
        if num:
            return num + 3
        else:
            return 'please insert number'
    except TypeError as err:
        return err
#


def guess_number(a, b):
    if a > 0 and a < 11:
        if a == b:
            print('you awesome')
            return True
    else:
        print('just input number from 1 - 10')


if __name__ == '__main__':

    b = random.randint(1, 10)
    print(b)

    while True:
        try:
            a = int(input('please gues random number  form  1 ke 10 '))
            if guess_number(a, b):
                break

        except TypeError:
            print('please enter a number')
        continue
