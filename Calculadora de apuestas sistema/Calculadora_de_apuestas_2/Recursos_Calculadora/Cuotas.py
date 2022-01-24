class Cuota:

    _posicion = 0

    def __init__(self, cuota):
        Cuota._posicion += 1
        self._cuota = cuota

    @property
    def posicion(self):
        return self._posicion

    @posicion.setter
    def posicion(self, posicion):
        self._posicion = posicion

    @property
    def cuota(self):
        return self._cuota

    @cuota.setter
    def cuota(self, cuota):
        self._cuota = cuota

    def __str__(self):
        return f'{Cuota._posicion}° Cuota: {self._cuota}'

if __name__ == '__main__':
    cuota1 = Cuota(1)
    print(cuota1)
    cuota2 = Cuota(2)
    print(cuota2)
