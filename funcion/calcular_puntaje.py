def calcular_puntaje(nota1, nota2, inasistencias, es_monitor):
    puntaje = (nota1 + nota2) / 2
    puntaje -= inasistencias * 0.1
    if es_monitor:
        puntaje += 0.5
    print('-')
    return round(puntaje, 2)

