# Escribe un programa que elimine todas las consonantes de una cadena de texto

consonantes = 'bcdfghklmnñprstvwxz'

cadena = input('Ingrese la cadena de texto: ')

for letra in cadena:
    if consonantes.find(letra.lower()) > -1:
        cadena = cadena.replace(letra, '')

print(f'Cadena nueva: {cadena}')