""" Calculadora de división: Escribe una función llamada division() que 
tome dos números como parámetros y realice la división del primero por 
el segundo. Asegúrate de manejar la excepción de división por cero y 
devuelve un mensaje adecuado en caso de ocurrir dicha excepción """

def division(num1, num2):
    resultado = num1 / num2
    print(f'El resultado entre {num1} y {num2} es {resultado:.1f}')

try:
    num1 = int(input('Ingrese el número 1: '))
    num2 = int(input('Ingrese el número 2: '))
    division(num1, num2)
except ZeroDivisionError:
    print('No se puede dividir por cero')