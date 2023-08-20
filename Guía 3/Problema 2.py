""" Conversor de temperatura: Crea una función llamada convertir_temperatura() 
que reciba una temperatura en grados Celsius y la convierta a grados Fahrenheit. 
Si se proporciona una temperatura inferior a -273.15°C (cero absoluto), lanza 
una excepción personalizada llamada ValorTemperaturaInvalidoError """

class ValorTemperaturaInvalidoError (Exception):
    pass

def convertir_temperatura(grados_c):
    print(f'La temperatura {grados_c}°C ha sido convertida a {(1.8 * grados_c) + 32}°F')

try:
    grados_c = float(input('Ingrese una temperatura en grados celsius: '))
    if grados_c < -273.15:
        raise ValorTemperaturaInvalidoError(f'La temperatura proporcionada {grados_c}°C es cero absoluto')
    else:
        convertir_temperatura(grados_c)
except ValorTemperaturaInvalidoError as error:
    print(error)