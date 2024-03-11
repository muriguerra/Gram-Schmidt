import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Função de inicialização da animação
def init():
    return []

# Função de animação
def update(frame):
    ax.view_init(elev=10, azim=frame)  # Defina o ângulo de rotação em torno do eixo z
    return []


# Criar figuras e eixos
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d', facecolor='black')  # Fundo preto


# Definir os vetores
a1 = np.array([1, 1, 0])  # Vetor 1
a2 = np.array([1, 0, 1])  # Vetor 2
a3 = np.array([0, 1, 1])  # Vetor 3
b2 = np.array([1/2, -1/2, 1])  # Vetor 2 projeção
b3 = np.array([-2/3, 2/3, 2/3])  # Vetor 3 projeção 
origem = np.array([0, 0, 0])  # Origem

ax.set_xlim([-1.5, 1.5])
ax.set_ylim([-1.5, 1.5])
ax.set_zlim([-0.5, 1.5])

# Adicionar os vetores ao gráfico
ax.quiver(origem[0], origem[1], origem[2], a1[0], a1[1], a1[2], color='red', arrow_length_ratio=0.1)  # Vetor 1 azul
ax.quiver(origem[0], origem[1], origem[2], b2[0], b2[1], b2[2], color='red', arrow_length_ratio=0.1)  # Vetor 3 azul
ax.quiver(origem[0], origem[1], origem[2], b3[0], b3[1], b3[2], color='red', arrow_length_ratio=0.1)  # Vetor 3 azul

# Adicionar o nome de cada vetor
ax.text(a1[0], a1[1], a1[2], 'b1', color='white', fontsize=12, ha='right')
ax.text(b2[0]+0.3, b2[1], b2[2], 'b2', color='white', fontsize=12, ha='right')
ax.text(b3[0]+0.3, b3[1], b3[2], 'b3', color='white', fontsize=12, ha='right')


# Adicionar rótulos aos eixos
ax.set_xlabel('Eixo X')
ax.set_ylabel('Eixo Y')
ax.set_zlabel('Eixo Z')

ax.xaxis.label.set_color('white')  # Cor do rótulo do eixo X
ax.yaxis.label.set_color('white')  # Cor do rótulo do eixo Y
ax.zaxis.label.set_color('white')  # Cor do rótulo do eixo Z

ax.tick_params(axis='x', colors='white')  # Cor dos valores do eixo X
ax.tick_params(axis='y', colors='white')  # Cor dos valores do eixo Y
ax.tick_params(axis='z', colors='white')  # Cor dos valores do eixo Z

corners_x = [a1[0], b3[0], 0]
corners_y = [a1[1], b3[1], 0]
corners_z = [a1[2], b3[2], 0]


corners = [list(zip(corners_x, corners_y, corners_z))]
ax.add_collection3d(Poly3DCollection(corners, alpha=0.25, linewidths=1, color='blue'))

corners_x = [b2[0], b3[0], 0]
corners_y = [b2[1], b3[1], 0]
corners_z = [b2[2], b3[2], 0]

corners = [list(zip(corners_x, corners_y, corners_z))]
ax.add_collection3d(Poly3DCollection(corners, alpha=0.25, linewidths=1, color='blue'))

corners_x = [a1[0], b2[0], 0]
corners_y = [a1[1], b2[1], 0]
corners_z = [a1[2], b2[2], 0]

corners = [list(zip(corners_x, corners_y, corners_z))]
ax.add_collection3d(Poly3DCollection(corners, alpha=0.25, linewidths=1, color='blue'))

# Criar animação
ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 2), init_func=init, blit=True)

ani.save('animation4.gif', writer='imagemagick', fps=30)

# Exibir o gráfico
plt.title('Plot 3D de 3 vetores')
ax.set_box_aspect(None, zoom=0.90)
plt.show()
