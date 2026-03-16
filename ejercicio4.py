numeros = []

def ordenarNumeros(numeros):
    numeros.sort(reverse=True)
    return numeros

while True:
    usuario = int(input('Ingrese un numero y ponga -1 cuando termine: '))
    if usuario != -1:
        numeros.append(usuario)
    else:
        break

print(ordenarNumeros(numeros))