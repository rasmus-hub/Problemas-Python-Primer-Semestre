""" Diseña un programa que lea el nombre, la nota de un examen y la nota 
media del curso, y le indique al estudiante si ha aprobado o suspendido el examen """

def ingreso_datos():
    nombre = input('Ingrese el nombre del alumno: ').capitalize().strip()
    nota_examen = float(input('Ingrese la nota del alumno: '))
    nota_media = float(input('Ingrese la nota media del curso: '))
    return nombre, nota_examen

nombre, nota_examen = ingreso_datos()

if nota_examen >= 5 and nota_examen <= 7:
    print(f'El alumno {nombre} ha aprobado el examen con nota {nota_examen}')
elif nota_examen < 5 and nota_examen >= 1:
    print(f'El alumno {nombre} ha suspendido el examen con nota {nota_examen}')
else:
    print(f'La nota {nota_examen} del alumno {nombre} es inválida')