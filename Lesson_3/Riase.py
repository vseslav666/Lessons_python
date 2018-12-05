def int_list(l):
    for i in l:
        if type(i) != int:
            raise TypeError
    sorted_list = sorted(l)
    print(sorted_list)
    return

unsort = [1, 1.2, 18]    
int_list(unsort)