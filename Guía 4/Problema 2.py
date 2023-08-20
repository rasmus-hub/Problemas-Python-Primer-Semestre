""" Inventario de herramientas (Mecánica): Crea un diccionario que represente 
el inventario de herramientas en un taller. Cada herramienta puede tener un 
nombre como clave y una cantidad como valor. Luego, permite agregar y eliminar 
herramientas, y muestra el inventario actualizado """

def inventario_actualizado():
    for herramienta, cantidad in inventario.items():
        print(f'{herramienta}: {cantidad}')
    print('----------------------------------------------')

inventario = {'Martillos': 15,
              'Destornilladores': 10,
              'Sierras': 12,
              'Alicates': 8}

opcion = None

while opcion != 3:
    opcion = int(input('[Taller]\n[1] Agregar Herramientas\n[2] Eliminar Herramientas\n[3] Salir\nElija una opción: '))

    match opcion:
        case 1:
            herramienta = input('Ingrese el nombre: ').title().strip()
            cantidad = int(input('Ingrese la cantidad: '))
            inventario[herramienta] = cantidad
            inventario_actualizado()
        case 2:
            herramienta = input('Ingrese el nombre: ').title().strip()
            inventario.pop(herramienta)
            inventario_actualizado()
        case _:
            if opcion != 3:
                print(f'La opción {opcion} es inválida')