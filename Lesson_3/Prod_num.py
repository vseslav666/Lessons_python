def product_num (*arg):
    prod = 1
    for i in arg:
        prod = prod * i
    print(prod)

product_num (1, 8, 16, 22)