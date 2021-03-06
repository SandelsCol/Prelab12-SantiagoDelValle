#Creación de la lista de promedios semanales
#La diferencia entre la mayor y la menor presión promedio semanal registrada
#Media y Mediana
#Clasificacion de semanas
#Promedio con respecto a temperaturas
#la desviación estándar en las mediciones de temperatura promedio semanal 
#Clasificación de temperaturas según el promedio
#Desviación promedio entre el rango rentable y el no rentable
# Desviación entre utilidad(Rango rentable y el no rentable) y el general  

import statistics


lista_Promedio=[110.06,107.89,108.45,108.49,109.03,110.11,109.87,119.38,119.35,116.34,117.73,120.01,118.19,119.53,117.09,118.03,118.65,117.47,117.49,109.65,110.44,110.51,107.38,109.26,106.18,109.36,106.61,105.16,110.11,105.48,108.37,107.59,108.91,108.35,109.57,122.56,124.44,125.97,121.03,121.22,122.41,122.15,124.52,123.35,125.76,121.08,122.29,105.42,110.67,107.73,105.76,107.85]

Promedio_Grados=[200.783333,196.111,197.583333,197.66667,198.738889,200.883333,200.405556,219.288889,219.227778,213.255556,216.011111,220.538889,216.927778,219.588889,214.444,216.111,217.778,215.494444,215.538889,199.966667,201.538889,201.677778,195.461111,199.194444,193.077778,199.38889,193.933333,191.05,200.883333,191.688889,197.427778,195.877778,198.5,197.383333,199.811111,225.605556,229.338889,232.377778,222.566667222,222.94444,225.305556,224.788889,229.494444,227.172222,231.961111,222.66667,225.066667,191.566667,201.994444,196.155556,192.244444,196.394444]

Promedio_Grados.sort()
Suma= sum(Promedio_Grados)
Div=len(Promedio_Grados)
Promedio= (Suma/Div)

print("El promedio fue de",Promedio,"F°")

Malpromedio=Promedio_Grados[:28]
Buenpromedio=Promedio_Grados[28:]
Longitud_Gp=len(Buenpromedio)
Longitud_Bp=len(Malpromedio)

print("Las temperaturas que estuvieron por encima del promedio fueron",Buenpromedio,"Creando un total de",Longitud_Gp)
print("Las temperaturas que estuvieron por debajo del promedio fueron",Malpromedio,"Creando un total de",Longitud_Bp)

DesviaciónBuena= statistics.stdev(Buenpromedio)
DesviaciónMala= statistics.stdev(Malpromedio)

print("El promedio de la Desviación por encima del promedio fue de",DesviaciónBuena,"F°")
print("El promedio de la Desviación por debajo del promedio fue de",DesviaciónMala,"F°")

PromedioDesviación= (DesviaciónBuena+DesviaciónMala)/2

print("El promedio de las dos desviaciones es de",PromedioDesviación,"F°")

Desviación_General=statistics.stdev(Promedio_Grados)

print("La desviación total fue de",Desviación_General,"F°")

Diferencia=  Desviación_General - PromedioDesviación

print("La diferencia entre las desviaciones fue de",Diferencia,"F°")