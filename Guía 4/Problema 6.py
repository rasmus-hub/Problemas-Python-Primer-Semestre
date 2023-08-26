""" Directorio telefónico (Vida cotidiana): Crea un diccionario donde cada 
clave sea el nombre de una persona y el valor sea su número de teléfono. 
Permite buscar un número de teléfono por nombre y mostrar todos los contactos 
en el directorio """

def mostrar_telefono(nombre):
    if opcion == 1:
        print(f'Nombre: {nombre} | Teléfono: {directorio[nombre]}')
    elif opcion == 2:
        for nombre, telefono in directorio.items():
            print(f'Nombre: {nombre} | Teléfono: {telefono}')


directorio = {'Gustavo' : 947832312,
              'Matias' : 943219097,
              'Juan' : 966890213,
              'Carlos' : 911239090}

opcion = None

while opcion != 3:
    nombre = None
    opcion = int(input('[Directorio Telefónico]\n[1] Buscar Teléfono\n[2] Mostrar Contactos\n[3] Salir\nElija una opción: '))
    print('------------------------------------------------------------------')
    match opcion:
        case 1:
            nombre = input('Ingrese el nombre de la persona: ').capitalize().strip()
            mostrar_telefono(nombre)
        case 2:
            mostrar_telefono(nombre)
        case _:
            if opcion != 3:
                print(f'La opción {opcion} es inválida')
    print('------------------------------------------------------------------')