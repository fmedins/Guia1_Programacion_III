palabra = input('Ingrese una palabra: ')

def esPalindromo(palabra):
    if palabra == palabra[::-1]:
        print('La palabra es un palindromo')
    else:
        print('La palabra no es un palindromo')

esPalindromo(palabra)