def this_function_print_stars():
    print ('I will print stars')
    print ('*****************')

this_function_print_stars()

def my_function (input_var1, input_var2):
    print(input_var1, input_var2)
    return input_var1 + input_var2

first_call = my_function(1, 1)
print (first_call)

second_call = my_function(1,123)
print(second_call)

def my_function (var1, var2, var3):
    print ("No way, I'm using this: {} {} {}" .format (
            var1, var2, var3))
    
new_call = my_function(1, 2, 3)
print(new_call)

def function_with_default_value (name, age=0, need_stars=False):
    message = '{} is {} years old' .format(name, age)
    print(message)
    
    if need_stars:
        print('******')
        