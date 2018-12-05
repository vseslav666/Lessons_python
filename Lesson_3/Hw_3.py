##############################################
try:
    a = int (input('Введите число' ))
    print(a)
    if a % 2 == 0:
        raise ValueError
    elif a < 0:
        raise TypeError
    elif a > 10:
        raise IndexError
except ValueError:
    print('Введено четное число')
except TypeError:
    print ('Введено число меньше нуля')
except IndexError:
    print ('Введено число больше 10')
    
##############################################

a = (1, 34, 'fsdfsdfsd', -6, 0.22)
try:
    i = int(input('Введите номер интерусующего вас объекта' ))
    print(a[i])
except IndexError:
     print ('объект с указанным номером отсутствует в списке')
except ValueError:
    print ('Номер объект должен быть числом')