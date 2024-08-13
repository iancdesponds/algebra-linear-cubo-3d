import pygame
import numpy as np

aresta = 80//2 # Divide por 2 porque o cubo tem o centro em (0, 0, 0), então a aresta é o dobro do tamanho
tamanho = largura, altura = 600, 600 # Tamanho da tela

# Face frontal
ponto_a = np.array([-aresta, aresta, aresta])
ponto_b = np.array([aresta, aresta, aresta])
ponto_c = np.array([aresta, -aresta, aresta])
ponto_d = np.array([-aresta, -aresta, aresta])
# Face traseira
ponto_e = np.array([-aresta, aresta, -aresta])
ponto_f = np.array([aresta, aresta, -aresta])
ponto_g = np.array([aresta, -aresta, -aresta])
ponto_h = np.array([-aresta, -aresta, -aresta])

# Matriz do cubo, onde cada coluna é um ponto
matriz_cubo = np.array([ponto_a, ponto_b, ponto_c, ponto_d, ponto_e, ponto_f, ponto_g, ponto_h]).T
matriz_cubo = np.vstack((matriz_cubo, np.ones(8)))


# Variáveis iniciais

d = 120 # Distância da câmera ao cubo

deg_x = 0 # Ângulo de rotação em x
deg_y = 0 # Ângulo de rotação em y
deg_z = 0 # Ângulo de rotação em z
variacao = 0 # Variação de velocidade controlada por "," e "."

rotaciona_x = True # Variável de controle de rotação em x
rotaciona_y = True # Variável de controle de rotação em y
rotaciona_z = True # Variável de controle de rotação em z

posx = 0 # Posição em x controlado por "a" e "d"
posy = 0 # Posição em y controlado por "w" e "s"

balls = 5 # Tamanho dos vértices


# Cor do cubo
r = 0
g = 255
b = 255
cor_cubo = (r,g,b)

# Variáveis de cor
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PINK = (255, 192, 203)
PURPLE = (128, 0, 128)
DARK_PURPLE = (75, 0, 130)
ORANGE = (255, 165, 0)
WHITE = (255, 255, 255)

# Lista de cores
colors = [CYAN, BLUE, GREEN, RED, PINK, PURPLE, ORANGE, WHITE]

# Variáveis para controlar a transição
color_index = 0
next_color_index = 1
color_transition = 0  # Valor entre 0 e 1, indica a transição entre as cores
mudanca_cor = True  # Ativa ou desativa a mudança de cor


pygame.init()
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Cubo 3D - Ian e Luigi")

# Relógio para controlar a velocidade de atualização da tela
clock = pygame.time.Clock() 

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Fecha o programa ao clicar no X
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: # Fecha o programa ao pressionar ESC
                pygame.quit()
                quit()

            elif event.key == pygame.K_PERIOD: # "." aumenta a velocidade de rotação
                variacao += 1
            elif event.key == pygame.K_COMMA: # "," diminui a velocidade de rotação
                variacao -= 1

            elif event.key == pygame.K_r: # Reseta a posição e a rotação
                deg_x, deg_y, deg_z = 0, 0, 0
                posx, posy = 0, 0
                rotaciona_x, rotaciona_y, rotaciona_z = True, True, True
                d = 120
                variacao = 0
                # Reseta a cor
                color_index = 0
                next_color_index = 1
                color_transition = 0
                mudanca_cor = False
                cor_cubo = CYAN


            elif event.key == pygame.K_x: # Ativa ou desativa a rotação em x
                rotaciona_x = not rotaciona_x
            elif event.key == pygame.K_y: # Ativa ou desativa a rotação em y
                rotaciona_y = not rotaciona_y
            elif event.key == pygame.K_z: # Ativa ou desativa a rotação em z
                rotaciona_z = not rotaciona_z

            elif event.key == pygame.K_t: # Ativa a rotação em x, y e z
                rotaciona_x, rotaciona_y, rotaciona_z = True, True, True
            elif event.key == pygame.K_f: # Desativa a rotação em x, y e z
                rotaciona_x, rotaciona_y, rotaciona_z = False, False, False

            elif event.key == pygame.K_c: # Ativa ou desativa a mudança de cor
                mudanca_cor = not mudanca_cor

        elif event.type == pygame.MOUSEWHEEL:
            if event.y == 1: # Rolar para cima aumenta a distância
                d += 5
            elif event.y == -1: # Rolar para baixo diminui a distância
                d -= 5
            # Limita a distância entre 5 e 800
            if d <= 0: 
                d = 5
            if d >= 800:
                d = 800
    
    # Limita o tamanho dos vértices entre 1 e 8
    balls = d//50
    if balls < 1:
        balls = 1
    if balls > 8:
        balls = 8

    keys = pygame.key.get_pressed() 
    # Controles de movimento e distância
    if keys[pygame.K_a] and posx <= 360: # Anda para a esquerda com limite de 360
        posx += 4
    if keys[pygame.K_d] and posx >= -360: # Anda para a direita com limite de -360
        posx -= 4

    if keys[pygame.K_w] and d < 800: # Se aproxima do cubo
        d += 5
    if keys[pygame.K_s] and d > 5: # Se afasta do cubo
        d -= 5

    if keys[pygame.K_UP] and posy >= -360: # Anda para cima com limite de -360
        posy -= 4
    if keys[pygame.K_DOWN] and posy <= 360: # Anda para baixo com limite de 360
        posy += 4

    # Adicionando mudança de direção da visão usando mouse
    pos_mouse = pygame.mouse.get_pos()
    
    # Transformando a matriz do cubo
            
    # Variáveis seno e cosseno da rotação em x
    sin_x = np.sin(np.radians(deg_x))
    cos_x = np.cos(np.radians(deg_x))

    # Variáveis seno e cosseno da rotação em y
    sin_y = np.sin(np.radians(deg_y))
    cos_y = np.cos(np.radians(deg_y))

    # Variáveis seno e cosseno da rotação em z
    sin_z = np.sin(np.radians(deg_z))
    cos_z = np.cos(np.radians(deg_z))

    # Translação em z, para afastar o cubo da câmera
    translacao_z = np.array([[1, 0, 0, -posx + (pos_mouse[0]-300)//2],
                             [0, 1, 0, -posy + (pos_mouse[1]-300)//2],
                             [0, 0, 1,                           100],
                             [0, 0, 0,                             1]])

    # Matriz de projeção
    matriz_p = np.array([[0,0,    0,-d],
                         [1,0,    0, 0],
                         [0,1,    0, 0],
                         [0,0,(-1/d),0]])

    # Translação em x e y, para centralizar o cubo
    translacao_xy = np.array([[1,0,largura/2 + posx],
                              [0,1, altura/2 + posy],
                              [0,0,               1]])

    # Matrizes de rotação em x, y e z
    rotacao_x = np.array([[1,    0,     0,0],
                          [0,cos_x,-sin_x,0],
                          [0,sin_x, cos_x,0],
                          [0,  0,       0,1]])

    rotacao_y = np.array([[ cos_y,0, sin_y,0],
                          [     0,1,     0,0],
                          [-sin_y,0, cos_y,0],
                          [     0,0,     0,1]])

    rotacao_z = np.array([[cos_z,-sin_z,0,0],
                          [sin_z, cos_z,0,0],
                          [    0,     0,1,0],
                          [    0,     0,0,1]])

    # Multiplicação das matrizes no cubo 3D
    X = matriz_p @ translacao_z @ rotacao_z @ rotacao_y @ rotacao_x @ matriz_cubo

    # Projeção em perspectiva
    projecao = np.ones((3, 8))
    for i in range(8):
        projecao[0][i] = X[1][i]/X[3][i]
        projecao[1][i] = X[2][i]/X[3][i]

    projecao = translacao_xy @ projecao

    # Rotação automática
    if rotaciona_x: # Rotação em x, se ativada
        deg_x += 1 + variacao
        if deg_x == 360:
            deg_x = 0
    if rotaciona_y: # Rotação em y, se ativada
        deg_y += 1 + variacao
        if deg_y == 360:
            deg_y = 0
    if rotaciona_z: # Rotação em z, se ativada
        deg_z += 1 + variacao
        if deg_z == 360:
            deg_z = 0

    ###########################################

    # Atualização da transição de cores
    if mudanca_cor:
        color_transition += 0.01  # Ajuste esse valor para controlar a velocidade da transição
        if color_transition >= 1:
            color_transition = 0
            color_index = (color_index + 1) % (len(colors) - 1)
            next_color_index = (color_index + 1) % (len(colors) - 1)

        # Interpolação entre as cores atual e próxima
        current_color = colors[color_index]
        next_color = colors[next_color_index]
        interpolated_color = [
            int(current_color[i] + (next_color[i] - current_color[i]) * color_transition)
            for i in range(3)
        ]

        cor_cubo = interpolated_color

    ###########################################

    # Fundo preto
    tela.fill((0, 0, 0))

    # Desenhando o cubo

    # Face traseira
    pygame.draw.line(tela, cor_cubo, (int(projecao[0][0]), int(projecao[1][0])), (int(projecao[0][1]), int(projecao[1][1])), width=3)
    pygame.draw.line(tela, cor_cubo, (int(projecao[0][1]), int(projecao[1][1])), (int(projecao[0][2]), int(projecao[1][2])), width=3)
    pygame.draw.line(tela, cor_cubo, (int(projecao[0][2]), int(projecao[1][2])), (int(projecao[0][3]), int(projecao[1][3])), width=3)
    pygame.draw.line(tela, cor_cubo, (int(projecao[0][3]), int(projecao[1][3])), (int(projecao[0][0]), int(projecao[1][0])), width=3)
    # Face frontal
    pygame.draw.line(tela, cor_cubo, (int(projecao[0][4]), int(projecao[1][4])), (int(projecao[0][5]), int(projecao[1][5])), width=3)
    pygame.draw.line(tela, cor_cubo, (int(projecao[0][5]), int(projecao[1][5])), (int(projecao[0][6]), int(projecao[1][6])), width=3)
    pygame.draw.line(tela, cor_cubo, (int(projecao[0][6]), int(projecao[1][6])), (int(projecao[0][7]), int(projecao[1][7])), width=3)
    pygame.draw.line(tela, cor_cubo, (int(projecao[0][7]), int(projecao[1][7])), (int(projecao[0][4]), int(projecao[1][4])), width=3)
    # Conexões
    pygame.draw.line(tela, cor_cubo, (int(projecao[0][0]), int(projecao[1][0])), (int(projecao[0][4]), int(projecao[1][4])), width=3)
    pygame.draw.line(tela, cor_cubo, (int(projecao[0][1]), int(projecao[1][1])), (int(projecao[0][5]), int(projecao[1][5])), width=3)
    pygame.draw.line(tela, cor_cubo, (int(projecao[0][2]), int(projecao[1][2])), (int(projecao[0][6]), int(projecao[1][6])), width=3)
    pygame.draw.line(tela, cor_cubo, (int(projecao[0][3]), int(projecao[1][3])), (int(projecao[0][7]), int(projecao[1][7])), width=3)
    # Vértices
    pygame.draw.circle(tela, cor_cubo, (int(projecao[0][0]), int(projecao[1][0])), balls)
    pygame.draw.circle(tela, cor_cubo, (int(projecao[0][1]), int(projecao[1][1])), balls)
    pygame.draw.circle(tela, cor_cubo, (int(projecao[0][2]), int(projecao[1][2])), balls)
    pygame.draw.circle(tela, cor_cubo, (int(projecao[0][3]), int(projecao[1][3])), balls)
    pygame.draw.circle(tela, cor_cubo, (int(projecao[0][4]), int(projecao[1][4])), balls)
    pygame.draw.circle(tela, cor_cubo, (int(projecao[0][5]), int(projecao[1][5])), balls)
    pygame.draw.circle(tela, cor_cubo, (int(projecao[0][6]), int(projecao[1][6])), balls)
    pygame.draw.circle(tela, cor_cubo, (int(projecao[0][7]), int(projecao[1][7])), balls)

    # Atualiza a tela
    clock.tick(60)
    pygame.display.update()
    pygame.display.flip()
