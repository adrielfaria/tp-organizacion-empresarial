import csv

ventas_totales = 0

with open("datos/ventas.csv", "r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)

    for fila in lector:
        cantidad = int(fila["cantidad"])
        precio = int(fila["precio_unitario"])

        total = cantidad * precio
        ventas_totales += total

print("Ventas totales:", ventas_totales)
