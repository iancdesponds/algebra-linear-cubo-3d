# Álgebra Linear - APS 4 - 2024.1 [Insper](https://www.insper.edu.br/pt/home)

## Autores do Projeto
- [Ian Cordibello Desponds](https://github.com/iancdesponds)
- [Luigi Orlandi Quinze](https://github.com/guizin-15)

## [Cubo 3D com Pygame](https://github.com/iancdesponds/algebra-linear-cubo-3d)
Neste projeto, implementamos a projeção de um cubo em 3D para uma tela 2D usando o algoritmo da pinhole camera. O objetivo é criar uma projeção em tempo real de um cubo em wireframe que pode girar em todas as direções.

## Processo de Criação
### Matriz do Cubo 3D
Para modelar o cubo em um espaço 3D, definimos inicialmente os 8 vértices que compõem o cubo. Cada vértice é representado por um vetor tridimensional. Em seguida, organizamos esses vértices em uma matriz onde cada coluna representa um ponto.

### Rotação nos Eixos x, y e z
As rotações são realizadas usando matrizes de rotação em torno dos eixos x, y e z. Para cada eixo, calculamos as funções trigonométricas seno e cosseno do ângulo de rotação e usamos esses valores para construir as respectivas matrizes de rotação.

$$
R_x = \begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & \cos(\theta) & -\sin(\theta) & 0 \\
0 & \sin(\theta) & \cos(\theta) & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
\hspace{0.5in}
R_y = \begin{bmatrix}
\cos(\theta) & 0 & \sin(\theta) & 0 \\
0 & 1 & 0 & 0 \\
-\sin(\theta) & 0 & \cos(\theta) & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
\hspace{0.5in}
R_z = \begin{bmatrix}
\cos(\theta) & - \sin(\theta) & 0 & 0 \\
\sin(\theta) & \cos(\theta) & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

Para aplicar a rotação em torno de um eixo, multiplicamos a matriz de rotação correspondente pela matriz do cubo 3D. A rotação é realizada em tempo real, e o ângulo de rotação é alterado automaticamente no loop principal do jogo.
Cada vértice do cubo é multiplicado pela matriz de rotação para obter a nova posição do vértice após a rotação. A matriz do cubo é atualizada com as novas posições dos vértices após a rotação.
Cada uma das rotações pode ser ativada ou desativada com as teclas `X`, `Y` e `Z`, respectivamente.

### Translação em x, y e z no Cubo 3D
Para afastar o cubo da câmera, aplicamos uma translação em z. Para mover o cubo para a esquerda ou direita ou para cima ou para baixo, aplicamos translações em x e y, respectivamente. As translações são realizadas usando matrizes de translação. Os valores de translação são definidos de acordo com os movimentos do usuário com as teclas e o mouse.

$$
T_z = \begin{bmatrix}
1 & 0 & 0 & x \\
0 & 1 & 0 & y \\
0 & 0 & 1 & z \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

$$
Onde:\\
$$

$$
x = -pos_x\text{ + (pos-mouse[0]-300)//2} \\
$$

$$
y = -pos_y\text{ + (pos-mouse[1]-300)//2} \\
$$

$$
z = 100 \text{ → distância da câmera ao centro do cubo}\\
$$

$$
pos_x = \text{movimento que o usuário fez com as teclas A e D} \\
$$

$$
pos_y = \text{movimento que o usuário fez com as teclas ↑ e ↓} \\
$$


### Transformação de Matriz para Projeção 2D
Para projetar o cubo em uma tela 2D, aplicamos a matriz de projeção em perspectiva. Essa matriz é responsável por converter as coordenadas tridimensionais em coordenadas bidimensionais, levando em consideração a distância da câmera ao cubo.

$$
\begin{bmatrix}
z_p \\
x_{p}w_{p} \\
y_{p}w_{p} \\
w_p \\
\end{bmatrix}= 
M_p\begin{bmatrix}
0 & 0 & 0 & -d \\
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & -\frac{1}{d} & 0
\end{bmatrix}
\begin{bmatrix}
x_o \\
y_o \\
z_o \\
1 \\
\end{bmatrix}
$$

$$
Onde:\\
\text{$d$ é a distância da câmera ao centro do cubo.}
$$

Portanto, para encontrar os valores de x e y na tela 2D, dividimos x_p e y_p por w_p.

$$
x = \frac{x_p w_p}{w_p}
$$

$$
y = \frac{y_p w_p}{w_p}
$$

### Translação da Projeção 2D em x e y
Para centralizar a projeção do cubo na tela e diminuir a distorção do cubo, aplicamos uma translação em x e y baseada no tamanho da tela (centralizar) e movimentos do usuário com as teclas.

$$
T_{xy} = \begin{bmatrix}
1 & 0 & x \\
0 & 1 & y \\
0 & 0 & 1\\
\end{bmatrix}\\
$$

$$
Onde:\\
$$

$$
x = \text{largura da tela} // 2 + pos_x\\
$$

$$
y = \text{altura da tela} // 2 + pos_y\\
$$

$$
pos_x = \text{movimento que o usuário fez com as teclas A e D} \\
$$

$$
pos_y = \text{movimento que o usuário fez com as teclas ↑ e ↓} \\
$$

### Como Executar o Jogo
Certifique-se de ter o Python instalado em seu sistema.

Baixe o código fonte do jogo.

Abra um terminal na pasta onde o código está localizado.

Execute o seguinte comando para instalar as bibliotecas Pygame e Numpy:
```bash
pip install -r requirements.txt
```

Em seguida, execute o seguinte comando para iniciar o jogo:
```bash
python main.py
```

## Controles

- Teclas `↑` e `↓`: Movimentam a câmera para cima, baixo, esquerda e direita.
- Teclas `W` e `S`: Aproximam e afastam a câmera do cubo, respectivamente.
- Teclas `A` e `D`: Movimentam a câmera para a esquerda e direita, respectivamente.
- Teclas `X`, `Y` e `Z`: Ativam ou desativam a rotação em torno dos eixos x, y e z, respectivamente.
- Tecla `T`: Ativa a rotação em torno de todos os eixos.
- Tecla `F`: Desativa a rotação em torno de todos os eixos.
- Tecla `R`: Reseta a posição e rotação do cubo.
- Tecla `.`: Aumenta a velocidade de rotação do cubo.
- Tecla `,`: Diminui a velocidade de rotação do cubo.
- Tecla `C`: Ativa ou desativa a mudança automática de cor do cubo.
- Movimento do mouse: Movimenta a câmera para cima, baixo, esquerda e direita.
- Scroll do mouse: Aproxima e afasta a câmera do cubo.
