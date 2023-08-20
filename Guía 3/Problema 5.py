""" Registro de usuarios: Implementa una función llamada registrar_usuario() 
que solicite al usuario ingresar su nombre y edad. Si la edad ingresada no 
es un número entero válido, lanza una excepción EdadInvalidaError. Si el 
usuario tiene menos de 18 años, lanza una excepción MenorEdadError """

class EdadInvalidaError (Exception):
    pass

class MenorEdadError (Exception):
    pass

def registrar_usuario():
    nombre = input('Ingrese el nombre: ')
    edad = input('Ingrese la edad: ')
    try:
        edad = int(edad)
    except ValueError:
        raise EdadInvalidaError (f'La edad "{edad}" es inválida')
    try:
        if edad < 18:
            raise MenorEdadError (f'La edad "{edad}" es menor a 18 años')
    except MenorEdadError as error:
        print(error)

try:
    registrar_usuario()
except EdadInvalidaError as error:
    print(error)
