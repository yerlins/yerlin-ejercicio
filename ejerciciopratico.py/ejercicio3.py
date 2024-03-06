
voltaje1 = float(input("Ingrese el primer voltaje: "))
voltaje2 = float(input("Ingrese el segundo voltaje: "))
voltaje3 = float(input("Ingrese el tercer voltaje: "))
voltaje4 = float(input("Ingrese el tercer voltaje: "))
voltaje5 = float(input("Ingrese el tercer voltaje: "))

promedio = (voltaje1 + voltaje2 + voltaje3) / 3

if promedio < 115:
    print("<VOLTAJE ALTO")
elif 115 <= promedio < 220:
    print("<ALTO VOLTAJE")
else:
    print("<PELIGRO=")

