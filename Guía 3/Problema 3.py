""" Validador de contraseña: Implementa una función llamada validar_contrasena() 
que reciba una contraseña como parámetro. La contraseña debe cumplir las siguientes 
condiciones: tener al menos 8 caracteres, contener al menos una letra mayúscula y al 
menos un número. Si la contraseña no cumple con estas condiciones, lanza una excepción 
ContrasenaInvalidaError """

import string

class ContrasenaInvalidaError (Exception):
    pass

def validar_contrasena(passwd):
    #Se crean variables para luego usarlas como comparacion
    mayusculas = string.ascii_uppercase
    numeros = string.digits

    # Se revisa si tiene al menos 8 caracteres
    if len(passwd) < 8:
        raise ContrasenaInvalidaError(f'La contraseña {passwd} tiene menos de 8 caracteres')
    else:
        print(f'La contraseña {passwd} tiene al menos 8 caracteres')
    print('----------------------------------------------')
    
    # Se revisa si tiene al menos una letra mayúscula
    for letra in passwd:
        if mayusculas.find(letra) > -1:
            mayusculas = mayusculas.replace(letra, '') # Se reemplaza la letra encontrada por un string vacío
    # Se compara el tamaño de la variable "mayusculas"
    if len(mayusculas) < 26:
        print(f'La contraseña {passwd} tiene al menos una letra mayuscula')
    else:
        raise ContrasenaInvalidaError(f'La contraseña {passwd} no tiene letras mayusculas')
    print('----------------------------------------------')
    
    #Se revisa si tiene al menos un número
    for letra in passwd:
        if numeros.find(letra) > -1:
            numeros = numeros.replace(letra, '')
    if len(numeros) < 10:
        print(f'La contraseña {passwd} tiene al menos un número')
    else:
        raise ContrasenaInvalidaError(f'La contraseña {passwd} no tiene números')
    print('----------------------------------------------')

try:
    validar_contrasena('Esnupi12')
except ContrasenaInvalidaError as error:
    print(error)