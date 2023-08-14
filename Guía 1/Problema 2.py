""" Diseña un programa que lea dos números enteros y calcule la suma, 
la resta, el producto y la división, según lo que elija el usuario """

def ingreso_numeros():
    num1 = int(input('Ingrese el 1er número: '))
    num2 = int(input('Ingrese el 2do número: '))
    return num1, num2

opcion = None

while opcion != 5:
    opcion = int(input('[1] Suma\n[2] Resta\n[3] Multiplicación\n[4] División\n[5] Salir\nIngrese una opción: '))
    print('-------------------------------------------------------')
    match opcion:
        case 1:
            num1, num2 = ingreso_numeros()
            print(f'La suma entre los números {num1} y {num2} es {num1 + num2}')
        case 2:
            num1, num2 = ingreso_numeros()
            print(f'La resta entre los números {num1} y {num2} es {num1 - num2}')
        case 3:
            num1, num2 = ingreso_numeros()
            print(f'El producto entre los números {num1} y {num2} es {num1 * num2}')
        case 4:
            num1, num2 = ingreso_numeros()
            print(f'La división entre los números {num1} y {num2} es {num1 / num2}')
        case _:
            if opcion != 5:
                print(f'La opción {opcion} es inválida')
    print('-------------------------------------------------------')