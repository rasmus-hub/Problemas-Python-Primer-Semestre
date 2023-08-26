""" Organizador de tareas diarias (Vida cotidiana): Crea una lista de tuplas, 
donde cada tupla contenga el nombre de una tarea y su hora de inicio. Luego, 
ordena la lista por hora de inicio y muestra las tareas en orden """

tareas = [('Tarea 1', '13:00 PM'),
          ('Tarea 3', '15:30 PM'),
          ('Tarea 5', '17:45 PM'),
          ('Tarea 2', '12:30 AM'),
          ('Tarea 4', '10:20 AM')]

tareas_ordenadas = sorted(tareas, key=lambda tareas: tareas[1])

for tarea in tareas_ordenadas:
    print(f'{tarea[0]}: {tarea[1]}')