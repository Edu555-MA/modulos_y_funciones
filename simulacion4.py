'''
Crea un módulo con las siguientes clases
Mesa
Silla
Lampara
las tres clases tiene como atributo color y precio.
En otro módulo importa únicamente la clase Silla y crea dos sillas. Una de color azul y otra roja con precios de 9.95

algoritmo funciona:5 puntos
algoritmo utiliza características de POO : 5 puntos
algoritmo controla errores y excepciones : 5 puntos
algoritmo aplica enumeradores o similar para Color : 5 puntos
algoritmo resuelve una mejora de funcionalidad : 5 puntos
'''

# muebles.py

# muebles.py

class Mueble:
    def __init__(self, color, precio):
        self.color = color
        self.precio = precio

class Mesa(Mueble):
    def __init__(self, color, precio, material):
        super().__init__(color, precio)
        self.material = material

class Silla(Mueble):
    def __init__(self, color, precio, material):
        super().__init__(color, precio)
        self.material = material

class Lampara(Mueble):
    def __init__(self, color, precio, tipo):
        super().__init__(color, precio)
        self.tipo = tipo

# uso_sillas.py


# Crear dos sillas
silla_azul = Silla(color='azul', precio=9.95, material='madera')
silla_roja = Silla(color='roja', precio=9.95, material='metal')

# Mostrar información de las sillas
print("Silla azul - Color:", silla_azul.color, "- Precio:", silla_azul.precio, "- Material:", silla_azul.material)
print("Silla roja - Color:", silla_roja.color, "- Precio:", silla_roja.precio, "- Material:", silla_roja.material)
