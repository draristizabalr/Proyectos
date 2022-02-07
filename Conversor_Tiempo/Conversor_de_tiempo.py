descarga_promedio = float(input('¿Cual es la velocidad promedio de descarga en mb/s?\n'))
peso_archivo = float(input('¿Cual es el tamaño del archivo en Gb?\n'))

tiempo_esperado = (peso_archivo * 1000) / descarga_promedio

tiempo = {'Horas': 0, 'Minutos': 0, 'Segundos': 0}
lista = []
while tiempo_esperado > 60:
    for i in range(3):
        lista.append(tiempo_esperado % 60)
        tiempo_esperado = tiempo_esperado // 60

    for keys in tiempo:
        tiempo[keys] = lista.pop()
        tiempo_esperado = tiempo_esperado // 60

print(tiempo)

