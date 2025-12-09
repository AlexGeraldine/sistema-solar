import pygame
import numpy as np

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

ESCALA = 0.5


def circulo_bresenham(surface, cor, centro, raio):
    x0, y0 = centro
    x = 0
    y = raio
    d = 3 - 2 * raio

    def plotar_simetrico(xc, yc, x, y):
        surface.set_at((xc + x, yc + y), cor)
        surface.set_at((xc - x, yc + y), cor)
        surface.set_at((xc + x, yc - y), cor)
        surface.set_at((xc - x, yc - y), cor)
        surface.set_at((xc + y, yc + x), cor)
        surface.set_at((xc - y, yc + x), cor)
        surface.set_at((xc + y, yc - x), cor)
        surface.set_at((xc - y, yc - x), cor)

    while x <= y:
        plotar_simetrico(x0, y0, x, y)
        if d < 0:
            d = d + 4 * x + 6
        else:
            d = d + 4 * (x - y) + 10
            y -= 1
        x += 1

def translacao(v1, v2):
    matrix = [(1, 0, v1[0]),
                (0, 1, v1[1]),
                (0, 1, 1)]
    return (
        matrix[0][0] * v2[0] + matrix[0][1] * v2[1] + matrix[0][2],
        matrix[1][0] * v2[0] + matrix[1][1] * v2[1] + matrix[1][2]
    )

def escala(v1, v2):
    matrix = [(v1[0], 0, 0),
                (0, v1[1], 0),
                (0, 0, 1)]
    return (
        matrix[0][0] * v2[0] + matrix[0][1] * v2[1] + matrix[0][2],
        matrix[1][0] * v2[0] + matrix[1][1] * v2[1] + matrix[1][2]
    )

def rotacao(ponto, angulo_graus, ancora=(0, 0)):
    theta = np.radians(angulo_graus)
    R = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  np.cos(theta)]
    ])

    ponto = np.array(ponto)
    ancora = np.array(ancora)

    ponto_transladado = ponto - ancora
    ponto_rotacionado = R @ ponto_transladado
    ponto_final = ponto_rotacionado + ancora

    return tuple(map(int, ponto_final))

posicao_sol = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# ----------------------------
# Mercúrio
posicao_mercurio = translacao(posicao_sol, (int(100*ESCALA), 0))
rotacao_mercurio = 0
translacao_mercurio = 0

# Vênus
posicao_venus = translacao(posicao_sol, (int(150*ESCALA), 0))
rotacao_venus = 0
translacao_venus = 0

# Terra
posicao_terra = translacao(posicao_sol, (int(200*ESCALA), 0))
rotacao_terra = 0
translacao_terra = 0

# Marte
posicao_marte = translacao(posicao_sol, (int(250*ESCALA), 0))
rotacao_marte = 0
translacao_marte = 0

# Júpiter
posicao_jupiter = translacao(posicao_sol, (int(350*ESCALA), 0))
rotacao_jupiter = 0
translacao_jupiter = 0

# Saturno
posicao_saturno = translacao(posicao_sol, (int(450*ESCALA), 0))
rotacao_saturno = 0
translacao_saturno = 0

# Urano
posicao_urano = translacao(posicao_sol, (int(550*ESCALA), 0))
rotacao_urano = 0
translacao_urano = 0

# Netuno
posicao_netuno = translacao(posicao_sol, (int(650*ESCALA), 0))
rotacao_netuno = 0
translacao_netuno = 0
# ----------------------------

tempo = 1000
anos = 0
pausado = False

pygame.font.init()
font = pygame.font.SysFont("Arial", 14)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Draw
    screen.fill("black")

    text1 = font.render(f"Anos: {int(anos)}", False, (255,255,255))
    screen.blit(text1, (0, 0))
    text1 = font.render(f"Velocidade: {(1000 / tempo):,.3f}x", False, (255,255,255))
    screen.blit(text1, (0, 16))

    if pausado:
        text1 = font.render("PAUSADO", False, (255,255,255))
        screen.blit(text1, (100, 0))

    pygame.draw.circle(screen, "white", posicao_sol, int(40*ESCALA))

    # Mercúrio
    circulo_bresenham(screen, "orange", (int(posicao_sol.x), int(posicao_sol.y)), int(100*ESCALA))
    pygame.draw.circle(screen, "orange", posicao_mercurio, int(10*ESCALA))
    pygame.draw.line(screen, "white", posicao_mercurio, rotacao((posicao_mercurio[0] + int(10*ESCALA), posicao_mercurio[1]), translacao_mercurio, posicao_mercurio), 2)

    # Vênus
    circulo_bresenham(screen, "yellow", (int(posicao_sol.x), int(posicao_sol.y)), int(150*ESCALA))
    pygame.draw.circle(screen, "yellow", posicao_venus, int(14*ESCALA))
    pygame.draw.line(screen, "black", posicao_venus, rotacao((posicao_venus[0] + int(10*ESCALA), posicao_venus[1]), translacao_venus, posicao_venus), 2)

    # Terra
    circulo_bresenham(screen, "blue", (int(posicao_sol.x), int(posicao_sol.y)), int(200*ESCALA))
    pygame.draw.circle(screen, "blue", posicao_terra, int(16*ESCALA))
    pygame.draw.line(screen, "white", posicao_terra, rotacao((posicao_terra[0] + int(10*ESCALA), posicao_terra[1]), translacao_terra, posicao_terra), 2)

    # Marte
    circulo_bresenham(screen, "red", (int(posicao_sol.x), int(posicao_sol.y)), int(250*ESCALA))
    pygame.draw.circle(screen, "red", posicao_marte, int(12*ESCALA))
    pygame.draw.line(screen, "white", posicao_marte, rotacao((posicao_marte[0] + int(10*ESCALA), posicao_marte[1]), translacao_marte, posicao_marte), 2)

    # Júpiter
    circulo_bresenham(screen, "brown", (int(posicao_sol.x), int(posicao_sol.y)), int(350*ESCALA))
    pygame.draw.circle(screen, "brown", posicao_jupiter, int(25*ESCALA))
    pygame.draw.line(screen, "white", posicao_jupiter, rotacao((posicao_jupiter[0] + int(20*ESCALA), posicao_jupiter[1]), translacao_jupiter, posicao_jupiter), 2)

    # Saturno
    circulo_bresenham(screen, "lightyellow", (int(posicao_sol.x), int(posicao_sol.y)), int(450*ESCALA))
    pygame.draw.circle(screen, "lightyellow", posicao_saturno, int(22*ESCALA))
    pygame.draw.line(screen, "black", posicao_saturno, rotacao((posicao_saturno[0] + int(20*ESCALA), posicao_saturno[1]), translacao_saturno, posicao_saturno), 2)

    # Urano
    circulo_bresenham(screen, "cyan", (int(posicao_sol.x), int(posicao_sol.y)), int(550*ESCALA))
    pygame.draw.circle(screen, "cyan", posicao_urano, int(18*ESCALA))
    pygame.draw.line(screen, "black", posicao_urano, rotacao((posicao_urano[0] + int(15*ESCALA), posicao_urano[1]), translacao_urano, posicao_urano), 2)

    # Netuno
    circulo_bresenham(screen, "lightblue", (int(posicao_sol.x), int(posicao_sol.y)), int(650*ESCALA))
    pygame.draw.circle(screen, "lightblue", posicao_netuno, int(18*ESCALA))
    pygame.draw.line(screen, "black", posicao_netuno, rotacao((posicao_netuno[0] + int(15*ESCALA), posicao_netuno[1]), translacao_netuno, posicao_netuno), 2)

    pygame.display.flip()

    #Process
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and tempo - 10 > 0:
        tempo -= 10

    elif keys[pygame.K_DOWN]:
        tempo += 10
    elif keys[pygame.K_SPACE]:
        pausado = True
    else:
        pausado = False

    dt = clock.tick(60) / tempo

    if not pausado:
        anos += dt / 5
        rotacao_mercurio += dt * 100
        translacao_mercurio += dt * 150
        posicao_mercurio = rotacao(translacao(posicao_sol, (int(100*ESCALA), 0)), rotacao_mercurio, posicao_sol)

        rotacao_venus += dt * 80
        translacao_venus += dt * 120
        posicao_venus = rotacao(translacao(posicao_sol, (int(150*ESCALA), 0)), rotacao_venus, posicao_sol)

        rotacao_terra += dt * 70
        translacao_terra += dt * 100
        posicao_terra = rotacao(translacao(posicao_sol, (int(200*ESCALA), 0)), rotacao_terra, posicao_sol)

        rotacao_marte += dt * 60
        translacao_marte += dt * 90
        posicao_marte = rotacao(translacao(posicao_sol, (int(250*ESCALA), 0)), rotacao_marte, posicao_sol)

        rotacao_jupiter += dt * 40
        translacao_jupiter += dt * 60
        posicao_jupiter = rotacao(translacao(posicao_sol, (int(350*ESCALA), 0)), rotacao_jupiter, posicao_sol)

        rotacao_saturno += dt * 30
        translacao_saturno += dt * 50
        posicao_saturno = rotacao(translacao(posicao_sol, (int(450*ESCALA), 0)), rotacao_saturno, posicao_sol)

        rotacao_urano += dt * 20
        translacao_urano += dt * 40
        posicao_urano = rotacao(translacao(posicao_sol, (int(550*ESCALA), 0)), rotacao_urano, posicao_sol)

        rotacao_netuno += dt * 10
        translacao_netuno += dt * 30
        posicao_netuno = rotacao(translacao(posicao_sol, (int(650*ESCALA), 0)), rotacao_netuno, posicao_sol)

pygame.quit()
