#import sys
#sys.path.insert(1, 'dsp-modulo')

from thinkdsp import SinSignal
from thinkdsp import CosSignal
from thinkdsp import decorate

#modulo para mostrar grafcas
import matplotlib.pyplot as plt

#Crear señal senoidal
seno = SinSignal(freq=400, amp=0.7, offset=0)
coseno = CosSignal(freq=800, amp=1.1, offset=0)

#Crear grafica en memoria
seno.plot()
decorate(xlabel='Tiempo (S)')
decorate(ylabel='Amplitud')

coseno.plot()

plt.show()