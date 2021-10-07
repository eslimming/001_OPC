import OpenOPC
import time
import pywintypes

pywintypes.datetime = pywintypes.TimeType

opc = OpenOPC.client()

print(opc.servers())

opc.connect('Matrikon.OPC.Simulation.1')
tags = ['Random.Int1', 'Bucket Brigade.Int1']
i = 1
while i <= 20:
    try:
        value = opc.read(tags)

        print(i, value)
    except OpenOPC.TimeoutError:
        print("TimeoutError occurred")

    time.sleep(1)
    i = i + 1

opc.close()
