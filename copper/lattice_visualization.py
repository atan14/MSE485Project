from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from traj_test import *

# Animate
def figax3d():
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    return fig, ax


def init(Ge_pos):
    pos = Ge_pos[0]
    x, y, z = zip(*pos)
    line.set_data(x, y)
    line.set_3d_properties(z, 'z')
    return line,


def draw_pos(ax, original_pos, Ge_pos, boron_pos, **kwargs):
    x, y, z = zip(*Ge_pos)
    line = ax.plot(x, y, z, marker='o', color='b', alpha=0.05, **kwargs)

    x, y, z = original_pos[boron_pos[0]]
    line = ax.scatter(x, y, z, marker='o', color='r', **kwargs)
    return line


def update_boron(iframe, line, original_pos, boron_pos):
    idx = boron_pos[iframe]
    x, y, z = original_pos[idx]
    line.set_data(x, y)
    line.set_3d_properties(z, 'z')

def update_Ge(iframe, line, Ge_pos):
    pos = Ge_pos[int(iframe/1.E15)]
    x, y, z = zip(*pos)
    line.set_data(x, y)
    line.set_3d_properties(z, 'z')

def update_line(iframe, line, original_pos, Ge_pos, boron_pos):
    update_boron(iframe, line, original_pos, boron_pos)
    update_Ge(iframe, line, Ge_pos)


def animate_pos(fig, ax, original_pos, Ge_pos, boron_pos, fps=60):
    from matplotlib.animation import FuncAnimation
    nframe = len(Ge_pos)
    line = draw_pos(ax, original_pos, Ge_pos, boron_pos)
    anim = FuncAnimation(fig, func=update_line,
                         frames=nframe, interval=100. / fps, init_func=init,
                         fargs=(original_pos, Ge_pos, line, boron_pos))
    return anim


if __name__ == '__main__':
    lattice_constant = 5.7629
    original_pos = sites
    Ge_pos = [site for idx, site in enumerate(sites) if idx % 2 == 0]
    boron_pos = [i.index('B') for i in types]

    fig, ax = figax3d()
    ani = animate_pos(fig, ax, original_pos, Ge_pos, boron_pos)
    plt.show()
