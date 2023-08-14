# Escribe un programa que reemplace la primera aparición de una subcadena en una cadena de texto

cadena = input('Ingrese la cadena de texto: ').split()

cadena[0] = input('Ingrese la nueva palabra: ')

cadena = ' '.join(cadena)

print(cadena)