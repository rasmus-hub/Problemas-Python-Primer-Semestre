# Escribe un programa que cuente la cantidad de palabras en una cadena de texto

palabras = 1
cadena = input('Ingrese la cadena de texto: ')

if cadena == '':
    print('No hay texto que revisar')
else:
    for letra in cadena:
        if letra == ' ':
            palabras += 1
    print(f'Palabras Encontradas: {palabras}')