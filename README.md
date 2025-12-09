🌌Simulação do Sistema Solar — Pygame

Este projeto é uma simulação simples do Sistema Solar utilizando Python e Pygame, representando os planetas orbitando o Sol com movimentos de rotação e translação, além de permitir controle de velocidade e pausa.

🛰️ Funcionalidades

🌞 Sol central fixo

🪐 Oito planetas com:

órbita circular usando o algoritmo de Bresenham

movimento de translação (órbita)

movimento de rotação (giro sobre o eixo)

⏱️ Controle de velocidade do tempo:

↑ acelera

↓ desacelera

⏸️ Tecla ESPAÇO pausa a simulação

📊 HUD exibindo:

anos simulados

velocidade atual

🧠 Como funciona
🔵 Desenho das órbitas

O programa utiliza o algoritmo Bresenham para círculos, garantindo um círculo suave pixel a pixel sem usar funções gráficas prontas.

↗️ Transformações geométricas implementadas

O código possui suas próprias funções de:

Translação

Escala

Rotação com âncora (usando matriz de rotação)

Essas funções simulam como gráficos 2D funcionam internamente, aplicando transformações sobre pontos.

🪐 Movimentação dos planetas

Cada planeta tem:

um raio orbital

uma velocidade de rotação

uma velocidade de translação

O movimento é atualizado usando dt (delta time), proporcional à velocidade configurada.

⏱️ Controle de tempo

A variável tempo controla a velocidade da simulação.
Quanto menor o valor, mais rápido tudo gira.

🎮 Controles
Tecla	Função
↑	Aumenta a velocidade (tempo mais rápido)
↓	Diminui a velocidade
ESPAÇO	Pausa/Despausa a simulação
ESC	Fecha a janela
📦 Dependências

Certifique-se de ter instalado:

pip install pygame numpy

▶️ Como rodar

Execute:

python simulacao_sistema_solar.py
