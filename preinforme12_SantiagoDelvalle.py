#Creación de la lista de promedios semanales
#La diferencia entre la mayor y la menor presión promedio semanal registrada
#Media y Mediana


lista_Promedio=[110.06,107.89,108.45,108.49,109.03,110.11,109.87,119.38,119.35,116.34,117.73,120.01,118.19,119.53,117.09,118.03,118.65,117.47,117.49,109.65,110.44,110.51,107.38,109.26,106.18,109.36,106.61,105.16,110.11,105.48,108.37,107.59,108.91,108.35,109.57,122.56,124.44,125.97,121.03,121.22,122.41,122.15,124.52,123.35,125.76,121.08,122.29,105.42,110.67,107.73,105.76,107.85]

def media(x,y):

    Media=(x/y) 
    print("La media de los promedios semanales es de",Media,"Kpa")

x=sum(lista_Promedio)
y=len(lista_Promedio)
media(x,y)

def median(z,o):

    lista_Promedio.sort()
    parte_1=lista_Promedio[z]
    parte_2=lista_Promedio[o]

    mediana= ((parte_1+parte_2)/2)

    print("La mediana de los promedios semanales es",mediana,"Kpa")

median(25,26)

Diferencia_Media_Mediana= 114.0442307692308 - 110.475

print("La diferencia entre la Media y la Mediana es de",Diferencia_Media_Mediana,"Kpa")

