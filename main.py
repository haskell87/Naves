import pygame
import random
import math  # importa a math como una clase estatica, no instanciable
from jugador import jugador  # importa a jugador como un objeto instanciable

import comunes

# Inicializa PyGame
pygame.init()

# Crear la pantalla
screen = pygame.display.set_mode((800, 600))

# Fondo
fondo = pygame.image.load("imagenes/fondo.jpg")

# Titulo e Icono
pygame.display.set_caption("AirMayhaem")
icono = pygame.image.load('imagenes/icono.png')  # https://www.flaticon.com/search?search-type=icons&word=arcade+space
pygame.display.set_icon(icono)

player = jugador("imagenes/player.png", 370, 480, screen,"imagenes/bullet.png")

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemycambioChico = []
enemyX_cambio = []
enemyY_cambio = []
enemy_cantidad = 3
for i in range(enemy_cantidad):
    enemyImg.append(pygame.image.load("imagenes/alien.png"))
    enemyX.append(random.randint(0, 800 - 64))
    enemyY.append(random.randint(50, 150))
    enemycambioChico = 0.3
    enemyX_cambio.append(enemycambioChico)
    enemyY_cambio.append(enemycambioChico)

# Variable Puntaje
puntaje_valor = 0
fuente = pygame.font.Font("freesansbold.ttf", 32)  # dafont.com
textX = 10
textY = 10


def puntaje_mostrar(x, y):
    puntaje = fuente.render("Puntaje: " + str(puntaje_valor), True, (255, 255, 255))
    screen.blit(puntaje, (x, y))


# Funcion que dibuja el enemigo
def enemy(enemyImg, x, y):
    screen.blit(enemyImg, (x, y))

# Loop principal del juego
ejecutandose = True
while ejecutandose:
    for event in pygame.event.get():  # recorre todos los eventos que suceden en la pantalla
        if event.type == pygame.QUIT:  # si el evento es el tratar de cerrar la pantalla, sale del loop
            ejecutandose = False

        # si se presiona una tecla, mover el jugador
        if event.type == pygame.KEYDOWN:
            player.tecla_presionada(event.key)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT :
            player.disparar()
        if event.type == pygame.KEYUP:
            player.tecla_levantada(event.key)

    # Dibujar Imagen de fondo
    screen.blit(fondo, (0, 0))

    # rotar, mover y dibujar el jugador
    player.dibujar(player.x, player.y,pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

    # Movemos el enemigo
    for i in range(enemy_cantidad):
        enemyY[i] += enemyY_cambio[i]
        enemyX[i] += enemyX_cambio[i]
        enemycambioChico *= random.random() + 1
        # restringimos los movimientos para que no se escape de la pantalla
        if enemyX[i] < 0:
            enemyX_cambio[i] = enemycambioChico
        elif enemyX[i] > (800 - 64):  # 800-64
            enemyX_cambio[i] = -enemycambioChico
        if enemyY[i] < 0:
            enemyY_cambio[i] = enemycambioChico
        elif enemyY[i] > (600 - 64):
            enemyY_cambio[i] = -enemycambioChico
        # Colision
        colision = comunes.esColision(enemyX[i], enemyY[i], player.bala.x, player.bala.y)
        if colision:
            balaY = player.y
            bala_estado = "cargada"
            puntaje_valor += 100

    # Dibujamos el enemigo
    for i in range(enemy_cantidad):
        enemy(enemyImg[i], enemyX[i], enemyY[i])

    puntaje_mostrar(textX, textY)

    # sin esta linea no actualiza el relleno de pantalla
    pygame.display.update()
