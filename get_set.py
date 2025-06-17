


class Cuenta_banco:
    def __init__(self,saldo):
        self._saldo = saldo

    @property   # este es el decorador de los getter
    def saldo(self):
        self._saldo


    @saldo.setter   ##este es el decorador de los setter
    def saldo(self, saldo):
        if saldo < 0:
            print("Saldo negativo no es posible ..")
            self._saldo = saldo


cuenta = Cuenta_banco(1000)
cuenta._saldo = 2000 # aqui se esta gatillando el setter cambiando el valor asignando el valor a una variable
print(cuenta._saldo) ### solo de esta forma devuelve el valor de 1000 , el property sólo transforma elargumento en una variable