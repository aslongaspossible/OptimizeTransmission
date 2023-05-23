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
from matplotlib.patches import ConnectionPatch


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

def plot_const(axes=None):
    data = np.loadtxt('const_dom.csv',delimiter=',')
    if axes==None:
        fig = plt.figure(figsize=(13, 17), dpi=300)
        ax1 = plt.subplot2grid((2,3), (1,0), colspan=3)
        ax2 = plt.subplot2grid((2,3), (0,0), colspan=2)
        ax3 = plt.subplot2grid((2,3), (0,2))
    else:
        fig, (ax1, ax2, ax3) = axes
    ax1.plot(data[:,0], data[:,3], '#d62728')
    ax1.set_xlim(0.,20.)
    ax1.set_xlabel(r"$M_0/\beta$")
    ax1.set_ylabel(r'$zT^\mathrm{max}$')
    ax1.set_ylim(0,10)
    ax1.text(0.2, 0.9, '(c)',transform=ax1.transAxes)
    ax1.text(0.32, 0.32, r"$(5.65,4)$",transform=ax1.transAxes, fontdict={'size':30})
    ax1.set_yticks([4, 8,])
    ax2.plot(data[:,0],data[:,1], color='#1f77b4',label=r'$x_1$')
    ax2.plot(data[:,0],data[:,2], color='#ff7f0e', label=r'$x_2$')
    ax2.legend()
    ax2.set_xlim(0, ax1.transData.inverted().transform([ax2.transAxes.transform([1,0])[0],0])[0])
    # ax2.set_xticks([0,5,10,15])
    ax2.set_xlabel(r".~~~$M_0/\beta$") # , loc='left'
    ax2.set_ylim(0,12)
    ax2.set_ylabel(r'$x=(\varepsilon-\mu)/(k_\mathrm{B}T)$')
    ax2.text(0.3, 0.9, '(a)',transform=ax2.transAxes)
    ax2.text(0.48, 0.48, r"$x_2=5.4$",transform=ax2.transAxes, fontdict={'size':30})
    ax2.text(0.48, 0.22, r"$x_1=2.1$",transform=ax2.transAxes, fontdict={'size':30})
    ax2.set_yticks([4, 8, 12])
    basepoint = data[188]
    boxy = np.linspace(0,12,num=1200)
    boxx = list(map(lambda y: 1 if y else 0, (boxy > basepoint[1]) & (boxy < basepoint[2])))
    ax3.plot(boxx, boxy, 'k')
    ax3.set_xlim(0, 1.5)
    ax3.set_xticks([0,1])
    ax3.set_xlabel(r'$\mathcal{T}(x)$')
    ax3.set_ylim(0,12)
    ax3.text(0.2, 0.9, '(b)',transform=ax3.transAxes)
    ax3.set_yticks([4, 8, 12])
    fig.add_artist(ConnectionPatch(
        xyA=(basepoint[0],basepoint[3]), xyB=(basepoint[0], basepoint[2]), 
        coordsA='data', coordsB='data', 
        axesA=ax1, axesB=ax2, 
        color='grey', ls='--'
    ))
    fig.add_artist(ConnectionPatch(
        xyA=(basepoint[0],basepoint[1]), xyB=(0,basepoint[1]), 
        coordsA='data', coordsB='data', 
        axesA=ax2, axesB=ax3, 
        color='#1f77b4', ls='--'
    ))
    fig.add_artist(ConnectionPatch(
        xyA=(basepoint[0],basepoint[2]), xyB=(0,basepoint[2]), 
        coordsA='data', coordsB='data', 
        axesA=ax2, axesB=ax3, 
        color='#ff7f0e', ls='--'
    ))
    return axes

def single_plot(x,y,axes=None):
    if axes is None:
        axes = plt.subplots(figsize=(13, 10))
    _, ax = axes
    ax.plot(x,y)
    return axes

def multi_plot(x, y_list, label_list, line_style_list=[], axes=None):
    if axes is None:
        axes = plt.subplots(figsize=(13, 10))
    _, ax = axes
    if line_style_list:
        for y, label, line_style in zip(y_list, label_list, line_style_list):
            ax.plot(x, y, line_style, label=label)
    else:
        for y, label in zip(y_list, label_list):
            ax.plot(x,y, label=label)
    ax.legend()
    return axes
