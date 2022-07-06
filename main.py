import numpy as np
import random
import variables as var
import funciones as f
import clases as c
import time

# creamos dos objetos de tablero ,uno para la persona y otro para la maquina
objeto_persona = c.Tablero('persona', var.ancho, var.largo, var.barcos)
objeto_maquina = c.Tablero('maquina', var.ancho, var.largo, var.barcos)
# el peimer turno es para la  persona,y print un tablero con los barcos de la persona

turno = 'persona'
print('Tus barcos:')
time.sleep(2)
print(objeto_persona.tablero_barcos)
#ahora empiza el juego
while True:
    # se pinta de quien es el turno
    print('Turno de: ' + turno)
    #si el turno es de la persona ,pintamos el tablero de la maquina,y pedimos la entrada de coordenadas
    if turno == 'persona':
        objeto_maquina.pintar()
        coordinadas_entrada = str(input("¿Dónde quieres disparar? Ejemplo: 1,1: ")).replace(".",",").split(',') #进入坐标返回的是一个列表
       
        # verifica si las coordenadas supera los limites o no, en caso de superar solicitamos nuevas coordenadas
        while int(coordinadas_entrada[0]) not in range(var.ancho) or int(coordinadas_entrada[1]) not in range(var.largo):
                print('Coordinada es invalida, introduce una nueva coordenada')
                coordinadas_entrada = str(input("¿Dónde quieres disparar? Ejemplo: 1,1: ")).replace(".",",").split(',')
        
        # verifica si esas coordenas hubo disparo o no, en caso de que si, solicitamos nuevas coordenadas. 
        while objeto_maquina.tiene_disparo(int(coordinadas_entrada[0]), int(coordinadas_entrada[1])):    
            print('Ya has disparado en esa coordenada, introduce una nueva coordenada')
            coordinadas_entrada = str(input("¿Dónde quieres disparar? Ejemplo: 1,1: ")).replace(".",",").split(',')
        
        # esta parte cuando se ha disparado al agua, retorna  false y pasa el turno a la maquina 
        if objeto_maquina.disparar(int(coordinadas_entrada[0]), int(coordinadas_entrada[1])) == False:
            turno = 'maquina'
        # se pinta finalmente el tablero de la maquina
        objeto_maquina.pintar()
        time.sleep(2)

    else: # en caso de que sea el turno de la maquina
        objeto_persona.pintar()# se pinta el tablero de la persona,y generar coordenadas aleatorias
        x = random.randint(0, var.ancho -1)
        y = random.randint(0, var.largo-1)

        # return self.tablero_disparos[x][y] == 'X' or self.tablero_disparos[x][y] == '-'
        #  este while generará un nueva coordenada mientras la coordenada aleatoria ya tenga un disparo
        while objeto_persona.tiene_disparo(x, y):
            x = random.randint(0, var.ancho -1)
            y = random.randint(0, var.largo -1)
        #se dispara a la coordenada generada si devuelve false parasamos el turno a la persona
        if objeto_persona.disparar(x, y) == False:
            turno = 'persona'
        #se vuelve a pintar  el tablero de disparos de la persona 
        objeto_persona.pintar()

   # una vez if acaba, se comprueba la vida de la persona y la maquina ,sse comprueba la vida si alguno llega
   # a 0 ,y el otro gana y se rompe el bucle ,y se pinta fin
    if objeto_persona.vidas == 0:
        print('Ganador: maquina')
        break
    if objeto_maquina.vidas == 0:
        print('Ganador: persona')
        break

print('FIN')
