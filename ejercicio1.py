def buscar(lista, usuario):
    return lista.index(usuario)

lista = [5, 20, 8, 9, 3]

usuario = int(input('Ingrese el numero que desea buscar en la lista: '))

print(f'El numero esta en la posicion {buscar(lista, usuario)}')

