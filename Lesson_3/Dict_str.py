def new_dict (dictionary):
    print(dictionary)
    new_dictionary = {}
    for key in dictionary:
        new_key = str(key)
        new_dictionary[new_key] = dictionary.get(key)
    print(new_dictionary)

a = {1 : 'one', 2 : 'two', 3 : 'three'}

new_dict(a)
