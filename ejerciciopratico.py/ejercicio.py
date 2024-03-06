voltajes = []
for i in range(5):
    voltaje = float(input("Ingrese el voltaje {}: ".format(i + 1)))
    voltajes.append(voltaje)

promedio = sum(voltajes) / len(voltajes)


if promedio > 220: 
    resultado = "<ALTO VOLTAJE"
else:
    resultado = "<VOLTAJE CORRECTO="


print(resultado, promedio)
