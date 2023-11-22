
'''
Actividad 2
En consola se piden las unidades y el precio.
Estos datos permiten calcular el subtotal.
Si el día de hoy es anterior al 15 de cada mes, se aplica
un descuento del 5%
Muestra el resultado el total de la factura.

algoritmo funciona:5 puntos
algoritmo utiliza mejora en argumentos : 5 puntos
algoritmo controla errores y excepciones : 5 puntos
algoritmo aplica funciones anónimas o recursividad : 5 puntos
algoritmo resuelve una mejora de funcionalidad : 5 puntos
'''

import datetime

def obtener_descuento(fecha_actual):
    # Verificar si el día es anterior al 15 del mes actual
    if fecha_actual.day < 15:
        return 0.05  # 5% de descuento
    else:
        return 0.0

def calcular_total(unidades, precio, descuento):
    subtotal = unidades * precio
    total = subtotal - (subtotal * descuento)
    return total

def obtener_valor_numerico(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("Error: Ingresa un valor numérico válido.")

def desea_repetir():
    respuesta = input("¿Quieres calcular otra factura? (s/n): ").lower()
    return respuesta == 's'

try:
    while True:
        # Solicitar las unidades y el precio
        unidades = obtener_valor_numerico("Introduce la cantidad de unidades: ")
        precio = obtener_valor_numerico("Introduce el precio por unidad: ")

        # Obtener la fecha actual
        fecha_actual = datetime.datetime.now()

        # Obtener el descuento
        descuento = obtener_descuento(fecha_actual)

        # Calcular el total
        total_factura = calcular_total(unidades, precio, descuento)

        # Mostrar el resultado
        print("\nDetalles de la Factura:")
        print(f"Unidades: {unidades}")
        print(f"Precio por unidad: {precio:.2f} euros")
        print(f"Subtotal: {unidades} unidades * {precio:.2f} euros = {total_factura:.2f} euros")
        print(f"Descuento aplicado: {descuento * 100:.2f}%")
        print(f"Total de la factura: {total_factura:.2f} euros")

        # Preguntar si desea repetir
        if not desea_repetir():
            break

except KeyboardInterrupt:
    print("\nOperación cancelada por el usuario.")
except Exception as e:
    print(f"Error inesperado: {e}")
