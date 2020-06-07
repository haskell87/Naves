import pygame
from jugador import jugador  # importa a jugador como un objeto instanciable
from Enemigo import Enemigo
import comunes

# Inicializa PyGame
pygame.init()

# Crear la pantalla
screen = pygame.display.set_mode((800, 600))

# Fondo
fondo = pygame.image.load("imagenes/fondo.jpg")

# Titulo e Icono
pygame.display.set_caption("AirMayhaem")
icono = pygame.image.load('imagenes/icono.png') # https://www.flaticon.com/search?search-type=icons&word=arcade+space
pygame.display.set_icon(icono)

player = jugador("imagenes/player.png", 370, 480, screen,"imagenes/bullet.png")

enemy_cantidad = 3
enemy = []

for i in range(enemy_cantidad):
    enemy.append(Enemigo("imagenes/alien.png",screen))

# Variable Puntaje
puntaje_valor = 0
fuente = pygame.font.Font("freesansbold.ttf", 32)  # dafont.com
textX = 10
textY = 10


def puntaje_mostrar(x, y):
    puntaje = fuente.render("Puntaje: " + str(puntaje_valor), True, (255, 255, 255))
    screen.blit(puntaje, (x, y))

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

    # Dibujar el jugador
    player.dibujar(player.x, player.y,pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

    # Movemos enemigos
    for i in range(enemy_cantidad):
        # Colisiones
        colision = comunes.esColision(enemy[i].x, enemy[i].y, player.bala.x, player.bala.y)
        if colision:
            player.bala.quieta = True
            puntaje_valor += 1
            enemy[i].morir()

        enemy[i].dibujar()

    puntaje_mostrar(textX, textY)

    # sin esta linea no actualiza el relleno de pantalla
    pygame.display.update()
