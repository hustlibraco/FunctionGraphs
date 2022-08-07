# -*- coding: utf-8 -*-
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axisartist.axislines import AxesZero

CURDIR = Path(__file__).resolve().parent

plt.style.use("seaborn-paper")
fig = plt.figure()
ax = fig.add_subplot(axes_class=AxesZero)

for direction in ["xzero", "yzero"]:
    # adds arrows at the ends of each axis
    ax.axis[direction].set_axisline_style("-|>")

    # adds X and Y-axis from the origin
    ax.axis[direction].set_visible(True)

for direction in ["left", "right", "bottom", "top"]:
    # hides borders
    ax.axis[direction].set_visible(False)

x = np.linspace(-2 * np.pi, 2 * np.pi, 200)
plt.xticks([-2 * np.pi, -3 * np.pi / 2, -np.pi, -np.pi / 2, 0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi],
           [r'-$2\pi$', r'-$3\pi/2$', r'-$\pi$', r'-$\pi/2$', '0', r'$\pi/2$', r'$\pi$', r'-$3\pi/2$', r'$2\pi$'])
plt.yticks([-1, 1])
ax.set_aspect(1)
f1, = ax.plot(x, np.cos(x), label="f(x)")
f2, = ax.plot(x, -np.sin(x), label="f'(x)", linestyle="dashed")
ax.legend(handles=[f1, f2], bbox_to_anchor=(1, 0), loc="upper right")
figpath = CURDIR.joinpath("cosx.png")
fig.savefig(figpath, bbox_inches="tight")
plt.show()
