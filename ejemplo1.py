#vamos a utilizar el contenido del módulo ejemplo 2
import ejemplo2
from ejemplo3 import Pais

ejemplo2.alumnos.update({"Luis":"dam"})
print(ejemplo2.alumnos)

#uso de funciones
ejemplo2.calcular_cubo()

#uso de clase
producto1=ejemplo2.Producto("camisa",50)

francia=Pais("France","Paris")