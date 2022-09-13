import imp
import numpy as np
from matplotlib import pyplot as plt
from scipy.io.wavfile import write
from scipy.fft import fft, fftfreq

SAMPLE_RATE = 44100 #HERTZ
DURATION = 5 #SECONDS
N = SAMPLE_RATE * DURATION #cantidad de muestras en el tono

def generar_onda_seno(freq, sample_rate, duration):
    x = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    frequencies = x * freq
    y = np.sin((2 * np.pi) * frequencies) #en radianes
    return x, y

x,y = generar_onda_seno(2, SAMPLE_RATE, DURATION)
plt.plot(x, y)
# plt.show() # mostrar la onda generada

#generar tonos

_, tono = generar_onda_seno(400, SAMPLE_RATE, DURATION)
_, ruido = generar_onda_seno(4000, SAMPLE_RATE, DURATION)
ruido = ruido * 0.3 #bajar intensidad de ruido

tono_conjunto = tono + ruido

# normalizar tono para entrar en 16 bits

tono_normalizado = np.int16((tono_conjunto / tono_conjunto.max()) * 32767)

plt.plot(tono_normalizado[:1000])
# plt.show()

# write("onda.wav", SAMPLE_RATE, tono_normalizado) # generar archivo de sonido

# calcular el espectro de frecuencias
yf = fft(tono_normalizado)
xf = fftfreq(N, 1 / SAMPLE_RATE)

plt.plot(xf, np.abs(yf))
plt.show()