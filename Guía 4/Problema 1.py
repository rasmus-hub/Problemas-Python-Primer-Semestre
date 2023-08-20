""" Registro de temperatura diaria: Crea un programa que permita ingresar la 
temperatura máxima registrada cada día de la semana y almacene estos valores 
en una lista. Luego, muestra la temperatura promedio y el día con la temperatura 
más alta """

dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
temperaturas = []
temperaturas_sumatoria = 0
temperatura_maxima = 0
dia_maximo = None

for dia in dias:
    temperatura = float(input(f'Ingrese la temperatura del día {dia}: '))
    temperaturas.append(temperatura)
    temperaturas_sumatoria += temperatura
    if dia == 'Lunes':
        dia_maximo, temperatura_maxima = dia, temperatura
    elif temperatura > temperatura_maxima:
        dia_maximo, temperatura_maxima = dia, temperatura
    print('----------------------------------------------')

print(f'Temperatura Promedio: {temperaturas_sumatoria / 7:.1f}°C\nDía Temperatura Alta: {dia_maximo} | {temperatura_maxima}°C')