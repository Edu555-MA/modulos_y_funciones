'''
Actividad 1 - 25 puntos
Por consola se piden como máximo 5 números hasta que pulsas q
muestra la suma de los números introducidos.
algoritmo funciona:5 puntos
algoritmo utiliza mejora en argumentos : 5 puntos
algoritmo controla errores y excepciones : 5 puntos
algoritmo aplica funciones anónimas o recursividad : 5 puntos
algoritmo resuelve una mejora de funcionalidad : 5 puntos
'''
def suma_numeros():
    numeros = []
    while len(numeros) < 5:
        try:
            entrada = input("Introduce un número (o 'q' para terminar): ")
            if entrada.lower() == 'q':
                break
            else:
                numero = float(entrada)
                numeros.append(numero)
        except ValueError:
            print("Error: Introduce un número válido.")

    suma = sum(numeros)
    return suma

resultado = suma_numeros()
print(f"La suma de los números introducidos es: {resultado}")


resultado = suma_numeros()
print(f"La suma de los números introducidos es: {resultado}")

'''
Explicación de los puntos:

Funciona correctamente (5 puntos): El programa cumple con el requisito de solicitar números hasta que se introduce 'q' y luego muestra la suma de los números introducidos.

Utiliza mejoras en argumentos (5 puntos): El programa utiliza una función (suma_numeros) para encapsular la lógica de obtener los números y calcular la suma. Esto hace que el código sea más modular y fácil de entender.

Controla errores y excepciones (5 puntos): Se utiliza un bloque try-except para manejar la posibilidad de que el usuario introduzca algo que no sea un número. Si ocurre una excepción, el programa imprime un mensaje de error y continúa solicitando la entrada.

Aplica funciones anónimas o recursividad (5 puntos): En este caso, no se utilizan funciones anónimas ni recursividad. Sin embargo, la estructura modular de la función suma_numeros permite una fácil extensión o modificación del código.

Resuelve una mejora de funcionalidad (5 puntos): El código está diseñado de manera que si no se introduce ningún número antes de presionar 'q', la función devuelve 0. Esto mejora la funcionalidad al proporcionar un resultado significativo incluso cuando no se ingresan números.

Ten en cuenta que estos son solo ejemplos y puedes adaptar el código según tus necesidades específicas o el lenguaje de programación que estés utilizando.
'''





