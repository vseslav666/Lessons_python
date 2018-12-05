import random
def exception(code):
    if code == 1:
        err = ValueError
    elif code == 2:
        err = TypeError
    elif code == 3:
        err = RuntimeError
    return err


try: 
    i = random.randrange(1,3)
    raise exception(i)
except ValueError:
    print('ValueError')
except TypeError:
    print ('TypeError')
except RuntimeError:
    print ('RuntimeError')