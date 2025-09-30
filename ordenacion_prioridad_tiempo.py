def comparator_tareas(tarea_a, tarea_b):
    prioridad_a = tarea_a['prioridad']
    prioridad_b = tarea_b['prioridad']
    tiempo_a = tarea_a['tiempo']
    tiempo_b = tarea_b['tiempo']
    
    #1. prioridad: ascendente (1 es la más alta/mejor) 
    if prioridad_a < prioridad_b:
        return True
    if prioridad_a > prioridad_b:
        return False
        
    #2. tiempo: ascendente (menor tiempo va primero)
    if tiempo_a < tiempo_b:
        return True
        
    #si prioridades y tiempos son iguales
    return False

def merge(izquierda, derecha):
    resultado = [] 
    i = j = 0
    
    while i < len(izquierda) and j < len(derecha):
        if comparator_tareas(izquierda[i], derecha[j]):
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
            
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

def merge_sort_tareas(lista):
    if len(lista) <= 1:
        return lista
        
    mitad = len(lista) // 2
    izquierda = lista[:mitad]
    derecha = lista[mitad:]
    
    izquierda_ordenada = merge_sort_tareas(izquierda)
    derecha_ordenada = merge_sort_tareas(derecha)
    
    return merge(izquierda_ordenada, derecha_ordenada)


#ejecución y prueba
tareas_simuladas = [
    {'nombre': 'Completar Informe', 'prioridad': 2, 'tiempo': 5},
    {'nombre': 'Enviar Email Masivo', 'prioridad': 1, 'tiempo': 1},
    {'nombre': 'Revisar Cuentas', 'prioridad': 3, 'tiempo': 8},
    {'nombre': 'Llamada Cliente A', 'prioridad': 1, 'tiempo': 2},
    {'nombre': 'Organizar Archivador', 'prioridad': 3, 'tiempo': 1},
    {'nombre': 'Preparar Presentación', 'prioridad': 2, 'tiempo': 3},
    {'nombre': 'Llamada Cliente B', 'prioridad': 1, 'tiempo': 1},
    {'nombre': 'Actualizar Software', 'prioridad': 2, 'tiempo': 5}
]

print("Lista de Tareas SIN Ordenar")
for t in tareas_simuladas:
    print(f"P: {t['prioridad']:<2} T: {t['tiempo']:<2}h Tarea: {t['nombre']}")

#aplicar el merge sort
tareas_ordenadas = merge_sort_tareas(tareas_simuladas)

print("\nLista de Tareas ORDENADA")
for t in tareas_ordenadas:

    print(f"P: {t['prioridad']:<2} T: {t['tiempo']:<2}h Tarea: {t['nombre']}")
