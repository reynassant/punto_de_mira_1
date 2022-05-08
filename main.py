import sys
import math
import matplotlib.pyplot as plt

RATE_OF_FIRE = 6  # Shots per second
AREA_OF_BULLET = 1/40  # Relative to drawing window
BULLET_MAX_ABS = {"x": math.inf, "y": math.inf}  # determines bullet size. Used for redrawing sight
RANDOM_FACTOR = 0.25  # Determines how much a weapons should deviates


def set_plot(lista_de_coordenadas):
    def on_close(event):
        print('User cancel')
        sys.exit()

    def maximo_abs(lista_de_coordenadas):
        max_coord = abs(max(max(lista_de_coordenadas)))
        min_coord = abs(min(min(lista_de_coordenadas)))

        return max(max_coord, min_coord)

    fig = plt.figure()
    fig.canvas.mpl_connect('close_event', on_close)

    max_coord = maximo_abs(lista_de_coordenadas) + 1
    plt.xlim(-1 * max_coord, max_coord)
    plt.ylim(-1 * max_coord, max_coord)

    plot_max_abs = {
        "x": abs(max(plt.xlim())),
        "y": abs(max(plt.ylim())),
    }

    BULLET_MAX_ABS["x"] = plot_max_abs["x"] * AREA_OF_BULLET
    BULLET_MAX_ABS["y"] = plot_max_abs["y"] * AREA_OF_BULLET

    plt.ylabel('Y')
    plt.xlabel('X')


def dibuja_punto_de_mira(color='k'):
    plt.plot(0, 0, f'{color}+')


def aleatoriza_tiro(coordenada):
    return coordenada

def dibuja_balas(lista_de_coordenadas, color='b'):
    def sobrescribe_punto_de_mira(coordenada):
        return abs(coordenada[0]) <= BULLET_MAX_ABS["x"] or \
                abs(coordenada[1]) <= BULLET_MAX_ABS["y"]

    PAUSE_TIME = 1 / RATE_OF_FIRE

    set_plot(lista_de_coordenadas)
    dibuja_punto_de_mira()

    for coordenada in lista_de_coordenadas:
        plt.plot(coordenada[0], coordenada[1], color=color, marker='o')
        if(sobrescribe_punto_de_mira(coordenada)):
            dibuja_punto_de_mira('r')
        plt.pause(PAUSE_TIME)

    plt.show()


if __name__ == '__main__':
    lista_de_coordenadas = []
    lista_de_coordenadas_aleatorizadas = []

    for r in range(RATE_OF_FIRE * 2):
        lista_de_coordenadas.append([r, r])

    for coordenada in lista_de_coordenadas:
        lista_de_coordenadas_aleatorizadas.append(aleatoriza_tiro(coordenada))

    dibuja_balas(lista_de_coordenadas_aleatorizadas)
