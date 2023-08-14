# Escribe un programa que convierta una cadena de texto en un acrónimo

import string

mayusculas = string.ascii_uppercase

acronimo = ''

cadena = 'Laughing Out Loud'

for letra in cadena:
    if mayusculas.find(letra) > -1:
        acronimo += letra

print(acronimo)