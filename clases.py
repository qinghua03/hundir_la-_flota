import funciones as f
import numpy as np
#definimos un clase tablero,para incluir en un solo sitio la logica del talero
# en el construcdor, asignamos los argumentos importantes e iniciamos atributos nesesarios para la logica
class Tablero:
    def __init__(self, id_jugador, ancho, largo, barcos):
        self.id_jugador = id_jugador
        self.ancho = ancho
        self.largo = largo
        self.vidas = 0
        self.tablero_barcos = np.full((ancho, largo), ' ')# 放船的表格
        self.tablero_disparos = np.full((ancho, largo), ' ')#对方放船，我方打的表格
        #con este for podemos  colocar los barcos que es un variable que contiene una lista de esloras
        # de barcos 
        for eslora in barcos:
            self.colocar_barco(eslora)
        
    def pintar(self):
        print('Tablero: ' + self.id_jugador)
        print(self.tablero_disparos)

    #este funcion colocar los barcos segun su eslora, con el bucle while se comprueba si ese lugar ya tiene 
    # barcos o no, en caso de que ya tiene barcos, hace que generamos nuevas posiciones de barcos, hasta 
    # que todas las coordenadas son validas. colocamos los barcos con el for
    def colocar_barco(self, eslora: int):
        coordenadas = f.barco_aleatorio(eslora, self.ancho, self.largo)
        while self.puedes_colocar_barco(coordenadas) == False:
            coordenadas = f.barco_aleatorio(eslora, self.ancho, self.largo)
        for x,y in coordenadas:
            self.tablero_barcos[x][y] = 'O'
            self.vidas = self.vidas + 1

    #Este funcion es para comprobar que en esas coordenadas no haya barcos.  
    def puedes_colocar_barco(self, coordenadas):#验证所有的坐标有没有重复放过
        for x,y in coordenadas:
            if self.tablero_barcos[x][y] == 'O':
                return False
        return True

    # Esta funcion sirve para disparar, si en el tablero barco hay un barco pintamos un X en tablero disparos
    # y se resta un vida. En caso de que no acertamos, se pinta un  quion. 
    def disparar(self, x, y):
        if self.tablero_barcos[x][y] == 'O':
            self.tablero_disparos[x][y] = 'X'
            self.vidas = self.vidas -1
            print('El barco de ' + self.id_jugador + ' ha sido golpeado. El turno no pasa')
            return True
        else:
            self.tablero_disparos[x][y] = '-'
            print("Ha dado al agua")
            return False

    # sirve para comprobar si en esas coordenadas hubo disparos o no  
    def tiene_disparo(self, x, y):#验证有没有重复射击同一个已经射过的坐标
        return self.tablero_disparos[x][y] == 'X' or self.tablero_disparos[x][y] == '-'


