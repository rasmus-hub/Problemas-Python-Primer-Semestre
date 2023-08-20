""" Generador de contraseña segura: Crea una función llamada generar_contrasena() 
que genere una contraseña segura de forma aleatoria. La contraseña debe tener al 
menos 10 caracteres, incluir letras mayúsculas, minúsculas, números y caracteres 
especiales. Utiliza la biblioteca random de Python y lanza una excepción personalizada 
si la generación de la contraseña falla """

import string
import random

class GeneracionFallida (Exception):
    pass

def generar_contrasena():
    passwd = ''
    caracteres = string.ascii_letters + string.digits + string.punctuation # Variable que almacena letras, números y caracteres especiales
    for caracter in range(random.randrange(10, 20)): # El randrange se usa para hacer todo tipo de contraseña teniendo en cuenta el tamaño requerido
        passwd += random.choice(caracteres) # Se elige un caracter aleatorio de la variable "caracteres", introduciendo cada uno en el string vacío
    return passwd

try:
    passwd = generar_contrasena()
    print(f'La contraseña generada: {passwd}')
except GeneracionFallida:
    print('Generacion Fallida')