#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
        except TypeError:  #Se genera cuando una operación o función se
            pass           #aplica a un objeto de tipo inapropiado.
        except ValueError: #Se genera cuando una función obtiene un
            pass           #argumento de tipo correcto pero valor incorrecto.
        else:
            count += 1
    print()
    return (count)
