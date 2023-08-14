""" Desarrollar un programa que permita cargar n números enteros y luego 
nos informe cuántos valores fueron pares y cuántos impares. Emplear el operador 
“%” en la condición de la estructura condicional (este operador retorna el resto 
de la división de dos valores, por ejemplo 11%2 retorna un 1) """

pares = 0
impares = 0
cantidad_numeros = int(input('Ingrese cantidad de números a introducir: '))

for numero in range(1, cantidad_numeros + 1):
    numero = int(input(f'Ingrese el número {numero}: '))
    if numero%2 == 0:
        pares += 1
    else:
        impares += 1

print(f'Total: {cantidad_numeros}\nPares: {pares}\nImpares: {impares}')