# Importamos directamente desde el archivo en la misma carpeta
from turtle_class import Tortuga

# Crear dos tortugas independientes
t1 = Tortuga()
t2 = Tortuga()

# Pruebas
t1.mover(10)
print("Posición de t1 después de mover 10:", t1.obtener_posicion())  # → 10

t2.mover(5)
print("Posición de t2 después de mover 5:", t2.obtener_posicion())    # → 5

t1.mover(20)
print("Posición de t1 después de mover 20 más:", t1.obtener_posicion())  # → 30
print("Posición de t2 (no cambió):", t2.obtener_posicion())            # → 5