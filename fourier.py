import imp
import numpy as np
from matplotlib import pyplot as plt
from scipy.io.wavfile import write
from scipy.fft import fft, fftfreq
from scipy.fft import rfft, rfftfreq
from scipy.fft import irfft

SAMPLE_RATE = 44100 #HERTZfrom scipy.fft import irfft
DURATION = 5 #SECONDS
N = SAMPLE_RATE * DURATION #cantidad de muestras en el tono

def generar_onda_seno(freq, sample_rate, duration):
    x = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    frequencies = x * freq
    y = np.sin((2 * np.pi) * frequencies) #en radianes
    return x, y

x,y = generar_onda_seno(2, SAMPLE_RATE, DURATION)
# plt.plot(x, y)
# plt.show() # mostrar la onda generada

#generar tonos

_, tono = generar_onda_seno(400, SAMPLE_RATE, DURATION)
_, ruido = generar_onda_seno(4000, SAMPLE_RATE, DURATION)
ruido = ruido * 0.3 #bajar intensidad de ruido

tono_conjunto = tono + ruido

# normalizar tono para entrar en 16 bits

tono_normalizado = np.int16((tono_conjunto / tono_conjunto.max()) * 32767)

# plt.plot(tono_normalizado[:1000])
# plt.show()

# write("onda.wav", SAMPLE_RATE, tono_normalizado) # generar archivo de sonido

# calcular el espectro de frecuencias
# como está definido va a mostrar las frecuencias -400, -4000, 400 y 4000 Hz
yf = fft(tono_normalizado) #fft calcula la transformada
xf = fftfreq(N, 1 / SAMPLE_RATE)

# plt.plot(xf, np.abs(yf)) #yf es un numero complejo, abs devuelve el módulo de ese numero
# plt.show()

# rfft usa numeros reales en lugar de complejos
yf = rfft(tono_normalizado)
xf = rfftfreq(N, 1 / SAMPLE_RATE)

# plt.plot(xf, np.abs(yf))
# plt.show()

# La maxima frequencia es la mitad del sample rate
points_per_freq = len(xf) / (SAMPLE_RATE / 2)

# La frequencia que buscamos es 4000 Hz
target_idx = int(points_per_freq * 4000)

yf[target_idx - 1 : target_idx + 2] = 0

# plt.plot(xf, np.abs(yf))
# plt.show()

new_sig = irfft(yf)

plt.plot(new_sig[:1000])
plt.show()

# guardar en archivo de audio

normalizado = np.int16(new_sig * (32767 / new_sig.max()))

write("clean.wav", SAMPLE_RATE, normalizado)

