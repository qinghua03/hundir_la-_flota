import numpy as np
import random

def barco_aleatorio(eslora, ancho, largo): 
    #en la parte de arriba es para las coordenadas no superen los limites del tablero
    origen = np.random.choice(["Norte", "Sur", "Este", "Oeste"])
    fila = None
    if origen == 'Norte':
        fila = random.randint(eslora -1, ancho -1)
    else:
        fila = random.randint(0, ancho - eslora)
    columna = None
    if origen == 'Este':
        columna = random.randint(0, largo - eslora)
    else:
        columna = random.randint(eslora -1, largo -1)
    coordenadas_barco = [[fila, columna]]
    # en la parte de abajo segun su orientacion para producir sus coordenadas,y finalmente retorna las coordenadas
    while len(coordenadas_barco) < eslora:
        if origen == "Norte":
            fila = fila - 1
        if origen == "Sur":
            fila = fila + 1
        if origen == "Este":
            columna = columna + 1
        if origen == "Oeste":
            columna = columna - 1
        
        coordenadas_barco.append([fila, columna])
    
    return coordenadas_barco