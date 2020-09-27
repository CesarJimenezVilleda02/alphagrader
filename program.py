def crea_lista(tam):
    lista = []
    for i in range(0,tam):
        list_value = int(input())
        lista.insert(i, list_value)
    return lista

def inicializa_lista(lista):
    default = int(input())
    for i in lista:
        lista.pop(i)
        lista.insert(i, default)
    return lista

def cuenta_impares(lista):
    for i in lista:
        if ((i % 2) == 0):
            count += 1
    return count

opción = int(input())


if (opción == 1):
    tamaño = int(input())
    print(crea_lista(tamaño))

if (opción == 2):
    tamaño = int(input())
    lista_ini = crea_lista(tamaño)
    print(inicializa_lista(lista_ini))

if (opción == 3):
    tamaño = int(input())
    lista_impares = crea_lista(tamaño)
    print(cuenta_impares(lista_impares))

if (opción == 4):
    tamaño = int(input())
    lista_invierte = crea_lista(tamaño).reverse()
    print(lista_invierte)

if (opción == 5):
    tamaño = int(input())
    lista_mayor = crea_lista(tamaño)
    lista_mayor.sort(reverse=True)
    print(lista_mayor[0])

