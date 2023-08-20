""" Validador de número positivo: Crea una función llamada validar_numero_positivo() 
que tome un número como parámetro y verifique si es positivo. Si el número no es 
positivo, lanza una excepción NumeroNoPositivoError """

class NumeroNoPositivoError (Exception):
    pass

def validar_numero_positivo(num):
    if num > 0:
        print(f'El número {num} es positivo')
    elif num == 0:
        print(f'El número {num} es neutral')
    else:
        raise NumeroNoPositivoError (f'El número {num} no es positivo')

try:
    num = int(input('Ingrese el número a verificar: '))
    validar_numero_positivo(num)
except NumeroNoPositivoError as error:
    print(error)