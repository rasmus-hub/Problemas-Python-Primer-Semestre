""" Una planta que fabrica perfiles de hierro posee un lote de n piezas.
Confeccionar un programa que pida ingresar por teclado la cantidad de 
piezas a procesar y luego ingrese la longitud de cada perfil; sabiendo 
que la pieza cuya longitud esté comprendida en el rango de 1.20 y 1.30 
son aptas. Imprimir por pantalla la cantidad de piezas aptas que hay en el lote. """

piezas_aptas = 0
piezas_noaptas = 0

cantidad_piezas = int(input('Ingrese la cantidad de piezas: '))

for pieza in range(1, cantidad_piezas + 1):
    longitud = float(input(f'Ingrese la longitud de la pieza {pieza}: '))
    if longitud >= 1.20 and longitud <= 1.30:
        piezas_aptas += 1
    else:
        piezas_noaptas += 1

print(f'Total Piezas: {cantidad_piezas}\nPiezas Aptas: {piezas_aptas}\nPiezas No Aptas: {piezas_noaptas}')