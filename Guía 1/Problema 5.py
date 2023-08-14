""" Se ingresan un conjunto de n alturas de personas por teclado. 
Mostrar la altura promedio de las personas """

sumatoria_alturas = 0

cantidad_personas = int(input('Ingrese la cantidad de personas: '))

for persona in range(1, cantidad_personas + 1):
    altura = float(input(f'Ingrese la altura de la persona {persona}: '))
    sumatoria_alturas += altura

print(f'La altura promedio de un total de {cantidad_personas} es {sumatoria_alturas / cantidad_personas:.2f}mts')