#Creación de la lista de promedios semanales
#La diferencia entre la mayor y la menor presión promedio semanal registrada
#Media y Mediana
#Clasificacion de semanas


lista_Promedio=[110.06,107.89,108.45,108.49,109.03,110.11,109.87,119.38,119.35,116.34,117.73,120.01,118.19,119.53,117.09,118.03,118.65,117.47,117.49,109.65,110.44,110.51,107.38,109.26,106.18,109.36,106.61,105.16,110.11,105.48,108.37,107.59,108.91,108.35,109.57,122.56,124.44,125.97,121.03,121.22,122.41,122.15,124.52,123.35,125.76,121.08,122.29,105.42,110.67,107.73,105.76,107.85]
lista_Promedio.sort()

Promedio_Inferior= lista_Promedio[:28]
Promedio_Superior= lista_Promedio[28:]

Semanas_Malas= len(Promedio_Inferior)
Semanas_Buenas= len(Promedio_Superior)

print("Los valores que estuvieron por debajo del promedio fueron..",Promedio_Inferior,"y tuvo un total de",Semanas_Malas,"Semanas")
print("Los valores que estuvieron por encima del promedio fueron..",Promedio_Superior,"y tuvo un total de",Semanas_Buenas,"Semanas")

