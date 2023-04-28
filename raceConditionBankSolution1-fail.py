import threading
import time
import random

movimientos = [-10000, 50000, -20000, 60000]

operaciones = []

class cuentaBancaria():
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def movimiento(self,monto):
        time.sleep(random.randint(1,5)/10)
        self.saldo += monto
    #    time.sleep(random.randint(1,5)/10)

cuenta = cuentaBancaria(20000)

print("Saldo Inicial:", cuenta.saldo)

for i in range(4):
    operacion = threading.Thread(target=cuenta.movimiento, args = (movimientos[i],))
    operacion.start()
    operaciones.append(operacion)

for i in range(2):
    operaciones[i].join()

print("Saldo Final:",cuenta.saldo)