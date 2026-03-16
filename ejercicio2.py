anio = int(input('Ingrese el anio que desea analizar: '))


def es_bisiesto(anio):
    if anio % 4 == 0:
        print('El anio es bisiesto')
    elif anio % 100 != 0:
        print('El anio no es bisiesto')
    elif anio % 400 == 0:
        print('El anio es bisiesto')

es_bisiesto(anio)