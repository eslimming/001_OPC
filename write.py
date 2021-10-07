import OpenOPC
import pywintypes
import time
import datetime

pywintypes.datetime = pywintypes.TimeType


def Escribir(Destino, count):
    opc = OpenOPC.client()
    opc.connect('Matrikon.OPC.Simulation.1')
    opc.write((Destino, count))
    print(Destino,i)
    opc.close()


i = 1
while i <= 10:
    try:
        Escribir('Bucket Brigade.Int1', i)
        i += 1
        time.sleep(2)
    except Exception as e:
        print([i, e, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')])
        i = 20000
