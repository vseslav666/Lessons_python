right_answer = ['Python', 'Гвидо Ван Россум', '2000']
question = ['Как называется язык который мы изучаем',
            'Как зовут автора языка',
            'В каком году была выпущена версия Pyton 2.0']


rigt_answer_counter = 0
wrong_answer_counter = 0

for i in range (0, len(right_answer)):
    print (question[i])
    user_answer = input()
    if (user_answer.lower()) == (right_answer[i].lower()):
        print ('Это верный ответ')
        rigt_answer_counter += 1
        
    else:
        wrong_answer_counter += 1
        print ('Ты выбрал неверную дверь, кожевенник')
        print ('Верный ответ', right_answer[i])
print ('Количество верных ответов', rigt_answer_counter )
print ('Количество неверных ответов', wrong_answer_counter )