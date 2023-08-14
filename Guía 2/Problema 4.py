# Escribe un programa que obtenga todas las palabras que terminan con una letra en particular en una cadena de texto

palabras_letras = []

cadena = input('Ingrese la cadena de texto: ').lower().split()

letra = input('Ingrese la letra: ').lower()

for palabra in cadena:
    if palabra.endswith(letra):
        palabras_letras.append(palabra)

print(f'Palabras que terminan con {letra}: {", ".join(palabras_letras)}')