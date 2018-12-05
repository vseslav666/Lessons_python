import random

EMPTY_MARK = 'x'


field = list(range(1, 16))
field.append(EMPTY_MARK)

def print_field():
    for i in range (0, 16, 4):
        print(field[i:i+4])

#empty_coord = field.index(EMPTY_MARK)
def move():
    empty_coord = field.index(EMPTY_MARK)
    print('Следующий ход')
    a = input()
    if a == 'a':
        empty_coord = (empty_coord - 1)
        field.remove(EMPTY_MARK)
        field.insert(empty_coord, EMPTY_MARK)
    if a == 'w':
        empty_coord = (empty_coord - 4)
        field.remove(EMPTY_MARK)
        field.insert(empty_coord, EMPTY_MARK)
    if a == 'd':
        empty_coord = (empty_coord + 4)
        field.remove(EMPTY_MARK)
        field.insert(empty_coord, EMPTY_MARK)
    if a == 'd':
        empty_coord = (empty_coord + 1)
        field.remove(EMPTY_MARK)
        field.insert(empty_coord, EMPTY_MARK)
#    return empty_coord
for i in range(1, 5):
    print_field()
    move()
    

    
