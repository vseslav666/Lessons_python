print ('Сортировка листа')
a = [87, 11, 1, -5, 8, 122]
print ('Исходный лист', a)
a = sorted(a)
print ('Отосротированный лист', a)
input()
###########################


print ('Словарь попарно') 
dict = {'one' : 1, 'two' : 2, 'three' : 3}
for key in dict:
    print (key, dict[key])
input() 
##########################  


print ('Максимальное и минимальное значение в кортеже')
tupel = (1.1, 0.815, 222.222, 2.0, 0.2)
print (tupel)
print ('Максимальное знаечение = ', max(tupel))
print ('Минимальное значение = ', min(tupel))
input()
##############################


print ('Вывод листа в строку')
a = '->'
address = ['Earth', 'Russia', 'Moskow']
print (a.join( address ))
input()
###############################


print ('Разделение строки')
Str = '/bin:/usr/bin:/usr/local/bin'
print (Str.split(':'))
input()
###############################


print ('Делимость числа на 7')
for i in range (1, 100):
    if i % 7 == 0:
        print (i)
input()
###############################   
    

print ('Вывод матрицы 3x3')
matrix = [[1, 2, 6],
          [4, 11, 8],
          [22, 16, 6],
        ]
s1 = []
s2 = []
s3 = []
i = 1
for row in matrix:
    print ('Строка номер ', (i), row)
    s1.append(row[0])
    s2.append(row[1])
    s3.append(row[2])
    i += 1

print ('Столбец номер 1', s1)
print ('Столбец номер 2', s2)
print ('Столбец номер 3', s3)
input()
###############################


print ('Вывод в консоль элементов списка с индексами')
List = ['d','1','gh','none','-_-','6']
print (List)
for element in List:
    print (element, '[', List.index(element), ']')
input()
###############################

print ('Удаление элементов из списка')
List = ['to-delete', 'please do not delete', 'very important data', 'to-delete' ]
print (List)
List.remove('to-delete')
print (List)
input()
###############################


print ('Цикл от 10 до одного')

for i in range (10, 0, -1):
    print(i)




