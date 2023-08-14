# Escribe un programa que obtenga la posición de la última aparición de una subcadena en una cadena de texto

cadena = input('Ingrese la cadena de texto: ').split()

ultima_palabra = cadena[-1]

posicion = cadena.index(ultima_palabra)

print(f'La ultima palabra "{ultima_palabra}" es la palabra {posicion + 1} de la cadena')
