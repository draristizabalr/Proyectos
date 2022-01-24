class Apuestas:
    def __init__(self, numero_apuestas):
        if self._validar_valor(numero_apuestas):
            self._numero_apuestas = numero_apuestas
        else:
            self._numero_apuestas = None

    @property
    def numero_apuestas(self):
        return self._numero_apuestas

    @numero_apuestas.setter
    def numero_apuestas(self, numero_apuestas):
        self._numero_apuestas = numero_apuestas

    def _validar_valor(self, valor):
        try:
            return True if valor == int(valor) else False
        except Exception as e:
            return False

    def __str__(self):
        return f'La cantidad de apuestas son: {self.numero_apuestas}'

if __name__ == '__main__':
    apuesta1 = Apuestas(3)
    print(apuesta1)
    apuesta2 = Apuestas(2.5)
    print(apuesta2)
    apuesta3 = Apuestas('a')
    print(apuesta3)

