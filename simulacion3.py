'''
Actividad 3
En consola pides número inicial.
En consola pides número final.
Muestra una lista con todos los números pares que hay entre
estos dos números.

algoritmo funciona:5 puntos
algoritmo utiliza mejora en argumentos : 5 puntos
algoritmo controla errores y excepciones : 5 puntos
algoritmo aplica funciones anónimas o recursividad : 5 puntos
algoritmo resuelve una mejora de funcionalidad : 5 puntos
'''
def obtener_numero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Por favor, ingresa un número válido.")

def main():
    while True:
        # Solicitar al usuario el número inicial y final
        numero_inicial = obtener_numero("Introduce el número inicial: ")
        numero_final = obtener_numero("Introduce el número final: ")

        # Asegurarse de que el número inicial sea par
        if numero_inicial % 2 != 0:
            numero_inicial += 1

        # Crear una lista con números pares entre el rango dado
        numeros_pares = list(range(numero_inicial, numero_final + 1, 2))

        # Mostrar la lista de números pares
        print("Números pares entre {} y {}: {}".format(numero_inicial, numero_final, numeros_pares))

        # Preguntar al usuario si desea volver a ejecutar el programa
        reiniciar = input("¿Quieres volver a iniciar? (s/n): ").lower()
        if reiniciar != 's':
            break

if __name__ == "__main__":
    main()
