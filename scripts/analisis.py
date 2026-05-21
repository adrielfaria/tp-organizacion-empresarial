import csv
import matplotlib.pyplot as plt

# Variables
ventas_totales = 0
ventas_por_producto = {}
ventas_por_mes = {}

# Leer CSV
with open("datos/ventas.csv", "r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)

    for fila in lector:
        producto = fila["producto"]
        cantidad = int(fila["cantidad"])
        precio = int(fila["precio_unitario"])
        fecha = fila["fecha"]

        total = cantidad * precio
        ventas_totales += total

        # Ventas por producto
        if producto in ventas_por_producto:
            ventas_por_producto[producto] += cantidad
        else:
            ventas_por_producto[producto] = cantidad

        # Ventas por mes
        mes = fecha[:7]

        if mes in ventas_por_mes:
            ventas_por_mes[mes] += total
        else:
            ventas_por_mes[mes] = total

# Producto más vendido
producto_mas_vendido = max(
    ventas_por_producto,
    key=ventas_por_producto.get
)

# Mostrar resultados
print("Ventas totales:", ventas_totales)
print("Producto más vendido:", producto_mas_vendido)

# Crear gráfico
meses = list(ventas_por_mes.keys())
totales = list(ventas_por_mes.values())

plt.figure(figsize=(8,5))
plt.bar(meses, totales)
plt.title("Ventas por mes")
plt.xlabel("Mes")
plt.ylabel("Monto vendido")
plt.savefig("resultados/grafico_ventas.png")

print("Gráfico guardado en resultados/")
