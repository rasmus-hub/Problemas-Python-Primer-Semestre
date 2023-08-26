""" Monitoreo de acciones (Bolsa de valores): Crea una lista de diccionarios, 
donde cada diccionario represente la información de una acción en la bolsa 
de valores. Cada diccionario debe contener claves como "nombre", "precio" y 
"variación". Luego, muestra la información de todas las acciones y ordena la 
lista según la variación """

acciones = [{'nombre' : 'Apple', 'precio' : 178.61, 'variación' : 2.23},
                 {'nombre' : 'Amazon', 'precio' : 133.26, 'variación' : 1.42},
                 {'nombre' : 'Nvidia CORP', 'precio' : 460.18, 'variación' : -11.45},
                 {'nombre' : 'Tesla', 'precio' : 238.59, 'variación' : 8.55}]

acciones_ordenadas = sorted(acciones, key=lambda acciones: acciones['variación'])

for accion in acciones_ordenadas:
    print(f'Nombre: {accion["nombre"]} | Precio: {accion["precio"]} | Variación: {accion["variación"]}')