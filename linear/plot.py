import numpy as np

import matplotlib as mpl
# %matplotlib inline
mpl.rcParams['text.usetex'] = True
mpl.rcParams['xtick.top'] = True
mpl.rcParams['xtick.direction'] = 'in'
mpl.rcParams['ytick.right'] = True
mpl.rcParams['ytick.direction'] = 'in'
import matplotlib.pyplot as plt
mpl.rcParams['font.size'] = 34
mpl.rcParams['lines.linewidth'] = 4
mpl.rcParams['patch.linewidth'] = 3
mpl.rcParams['axes.linewidth'] = 2
mpl.rcParams['xtick.major.size'] = 15
mpl.rcParams['xtick.major.width'] = 2
mpl.rcParams['ytick.major.size'] = 15
mpl.rcParams['ytick.major.width'] = 2
# from matplotlib.patches import ConnectionPatch


def gaussian(x, mu, sig):
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.))) / sig / np.sqrt(2*np.pi)

def step_vs_delta(
    axes=None, 
    delta_label="Mahan's limit", 
    subplot_label=None
):
    b2fb = 0.43922883989064515
    beta = np.linspace(1, 0, num=1000, endpoint=False)
    Mahan = b2fb / beta
    # b = 2.4
    # a1 = I1stp**2 / I0stp # 0.9865492318944619
    # a2 = I2stp - a1 # 0.08681796767013206
    a1 = 0.9865492318944619
    a2 = 0.08681796767013206
    step = a1 / (a2 + beta)
    # matplotlib.rcParams.update({'font.size': 34})
    if axes is None:
        axes = plt.subplots(figsize=(13, 10))
    _, ax = axes
    if subplot_label is not None:
        ax.text(0.2, 0.9, subplot_label,transform=ax.transAxes)
    ax.plot(beta, step, 'r', label=r'step function')
    ax.plot(beta, Mahan, 'k--', label=delta_label)
    ax.set_xlabel(r"$\beta$") # 
    ax.set_ylabel(r'$zT^\mathrm{max}$')
    ax.legend()
    ax.set_ylim([0,9])
    ax.set_xlim([0,1])
    ax.set_xticks([0.2,0.4,0.6,0.8,1.0])
    return axes
# step_vs_delta()

def plot_delta_step(
    axes=None, 
    x_range=np.linspace(-1,7,1000),
    subplot_label=None
):
    b = 2.4
    delta = gaussian(x_range, b, .01)
    step = np.heaviside(x_range-b, 1/2)
    if axes is None:
        axes = plt.subplots(figsize=(13, 10))
    _, ax = axes
    if subplot_label is not None:
        ax.text(0.2, 0.9, subplot_label,transform=ax.transAxes)
    ax.plot(x_range, delta, 'k', label=r'delta function')
    ax.plot(x_range, step, 'r', label=r'step function')
    ax.set_xlim([x_range.min(), x_range.max()])
    ax.set_xlabel(r"$(E-\mu)/(k_\mathrm{B}T)$")
    ax.set_ylim([0,2]) # 
    ax.set_ylabel(r'$M(E)\mathcal{T}(E)$')
    ax.set_yticks([0, 1, 2])
    ax.legend()
    return axes
# plot_delta_step()