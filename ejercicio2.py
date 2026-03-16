anio = int(input('Ingrese el anio que desea analizar: '))

try:
    def es_bisiesto(anio):
        if anio % 4 == 0:
            print('El anio es bisiesto')
        elif anio % 100 != 0:
            print('El anio no es bisiesto')
        elif anio % 400 == 0:
            print('El anio es bisiesto')

except ValueError:
    print('El valor ingresado no es un numero entero')

print(es_bisiesto(anio))