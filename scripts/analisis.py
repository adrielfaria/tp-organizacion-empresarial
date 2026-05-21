import csv

ventas_totales = 0
ventas_por_producto = {}
ventas_por_mes = {}

with open("datos/ventas.csv", "r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)

    for fila in lector:
        producto = fila["producto"]
        cantidad = int(fila["cantidad"])
        precio = int(fila["precio_unitario"])
        fecha = fila["fecha"]

        total = cantidad * precio
        ventas_totales += total

        if producto in ventas_por_producto:
            ventas_por_producto[producto] += cantidad
        else:
            ventas_por_producto[producto] = cantidad

        mes = fecha[:7]

        if mes in ventas_por_mes:
            ventas_por_mes[mes] += total
        else:
            ventas_por_mes[mes] = total

producto_mas_vendido = max(
    ventas_por_producto,
    key=ventas_por_producto.get
)

print("Ventas totales:", ventas_totales)
print("Producto más vendido:", producto_mas_vendido)

print("Ventas por mes:")
print(ventas_por_mes)
