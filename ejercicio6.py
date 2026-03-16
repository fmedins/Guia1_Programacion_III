def vocal(frase):
    vocales = 'aeiouAEIOU'
    contador = 0
    for letra in frase:
        if letra in vocales:
            contador += 1
    return contador

frase = input('Ingrese una frase: ')

res = vocal(frase)

print(f'La cantidad de vocales en la frase es: {res}')