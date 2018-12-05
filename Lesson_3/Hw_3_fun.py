def fun(a, b):
    if (a > 0) and (b > 0):
        print(a+b)
    elif (a < 0) and (b < 0):
        print(a-b)
    elif (a < 0) and (b > 0):
        print(0)
    elif (a > 0 ) and (b < 0):
        print(0)
    elif (a == 0) or (b == 0):
        print ('Введен неверный аргумент')
fun (-3, 0)

##############################
def fun (a, b ,c):
    lst = [a, b, c]
    lst.remove(min(lst))
    print (lst)  
fun(1, 16, 3)

#################################
