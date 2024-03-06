
import math

lado = float(input("Ingrese la longitud de un lado del triángulo equilátero: "))

if lado <= 0:
    print("<DATOS NO VÁLIDOS")
else:
    
    area = (math.sqrt(3) / 4) * lado ** 2

    if area > 1000:
        print("<DATOS NO VÁLIDOS=")
    else: 
        print("El área del triángulo equilátero es:", area)



