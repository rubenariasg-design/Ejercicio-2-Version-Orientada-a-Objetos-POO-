class Tortuga:
    def __init__(self):
        self._posicion_x = 0

    def mover(self, distancia):
        self._posicion_x += distancia

    def obtener_posicion(self):
        return self._posicion_x