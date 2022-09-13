import imp
import numpy as np
from matplotlib import pyplot as plt

SAMPLE_RATE = 44100 #HERTZ
DURATION = 5 #SECONDS

def generar_onda_seno(freq, sample_rate, duration):
    x = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    frequencies = x * freq
    y = np.sin((2 * np.pi) * frequencies) #en radianes
    return x, y