#Сортировка листа
a = [87, 11, 1, -5, 8, 122]
a = sorted(a)
print (a)

#Словарь попарно 
dict = {'one' : 1, 'two' : 2, 'three' : 3}
for key in dict:
    print (key, dict[key])
    
    
# Tuple min, max
tupel = (1.1, 0.815, 222.222, 2.0, 0.2)
print ('Максимальное знаечение = ', max(tupel))
print ('Минимальное значение = ', min(tupel))


# Вывод листа в строку
a = '->'
address = ['Earth', 'Russia', 'Moskow']
print (a.join( address ))

#Разделение строки
Str = '/bin:/usr/bin:/usr/local/bin'
print (Str.split(':'))

#Делимость числа на 7
for i in range (1, 100):
    if i % 7 == 0:
        print (i)




