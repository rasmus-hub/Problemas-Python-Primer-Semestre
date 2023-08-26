""" Gestión de clientes (Bancos): Crea un diccionario donde cada clave sea el 
nombre de un cliente y el valor sea una tupla con su saldo actual y número de 
cuenta. Permite agregar nuevos clientes, realizar operaciones de depósito y 
retiro de dinero, y mostrar la información de un cliente en particular """

def mostrar_clientes(nombre):
    if opcion == 1:
        for clave, tupla in clientes.items():
            print(f'Nombre: {clave} | Saldo Actual: {tupla[0]} | N° Cuenta: {tupla[1]}')
    elif opcion == 2 or opcion == 3:
        print(f'Nombre: {nombre} | Saldo Actual: {clientes[nombre][0]} | N° Cuenta: {clientes[nombre][1]}')
    print('------------------------------------------------------------------')

def depositar_retirar(nombre, saldo):
    clientes[nombre] = list(clientes[nombre])
    clientes[nombre][0] += saldo

clientes = {'Gustavo' : (350000, 5101),
            'Matias' : (250000, 3092),
            'Juan' : (300000, 2535)}

opcion = None

while opcion != 4:
    opcion = int(input('[Banco]\n[1] Agregar Clientes\n[2] Depositar o Retirar Dinero\n[3] Buscar Cliente\n[4] Salir\nElija una opción: '))

    match opcion:
        case 1:
            nombre = input('Ingrese el nombre del cliente: ').capitalize().strip()
            saldo = int(input('Ingrese saldo actual: '))
            numero_cuenta = int(input('Ingrese N° Cuenta: '))
            clientes[nombre] = (saldo, numero_cuenta)
            mostrar_clientes(nombre)
        case 2:
            nombre = input('Ingrese el nombre del cliente: ').capitalize().strip()
            saldo = int(input('Ingrese dinero a depositar(+) o retirar(-): '))
            depositar_retirar(nombre, saldo)
            mostrar_clientes(nombre)
        case 3:
            nombre = input('Ingrese el nombre del cliente: ').capitalize().strip()
            mostrar_clientes(nombre)
        case _:
            if opcion != 4:
                print(f'La opción {opcion} es inválida')