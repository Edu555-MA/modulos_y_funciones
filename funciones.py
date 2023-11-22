#capitulo 10 - pagina 204

#user functions
def sumar(i,j): #parametro de entrada
    return i+j #salida - output

suma_anonima=lambda i,j:i+j
print(F"el total de la suma anónima con lamba es {suma_anonima}")

def sumar_default(i,j,k=15): #default argument
    return i+j+k



def sumar_variables(*args): #variable argument
    total=0
    for i in args:
        total+=i
    return total

suma=sumar(4,5) #llamada a la funcion
print(f"el total de la suma es {suma}")

suma2=sumar_default(4,5)
print(f"el total de la suma con argumentos es {suma2}")

suma3=sumar_variables(5,9,4,7)
print(f"la suma total de una funcion con argumentos variables es {suma3}")

#recursividad : una función que se llama a asi misma
def factorial(n):
    if n==1:
        return n
    elif n<=0:
        print("no hay factorial para 0 o menor que 0")
    else:
        return n*factorial(n-1) #recursividad porq se llama a si mismo

resultado_factorial=factorial(-3)
print(f"el factorial es {resultado_factorial}")

