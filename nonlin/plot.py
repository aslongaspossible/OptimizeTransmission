import matplotlib
matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['xtick.top'] = True
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.right'] = True
matplotlib.rcParams['ytick.direction'] = 'in'
matplotlib.rcParams['lines.linewidth'] = 4
matplotlib.rcParams['patch.linewidth'] = 3
matplotlib.rcParams['axes.linewidth'] = 2
matplotlib.rcParams['xtick.major.size'] = 15
matplotlib.rcParams['xtick.major.width'] = 2
matplotlib.rcParams['ytick.major.size'] = 15
matplotlib.rcParams['ytick.major.width'] = 2
matplotlib.rcParams['font.size'] = 34
import matplotlib.pyplot as plt
import numpy as np
lin_data=np.loadtxt('lin_data.csv',delimiter=',')
nonlin_data=np.load('arith_mean_correct.npz')
t2s = nonlin_data['t2s']
aMs = nonlin_data['aMs']
nonlin_results = nonlin_data['results']
# from ipywidgets import interact, widgets, Layout


def rescale_plot_zT(order=1, xlim=100, ylim=40, linewidth=4, xlabel=r"$\alpha'M_0$"):
    fig, ax = plt.subplots(figsize=(17, 10))
    for index_t2 in [0, 14, 29, 49, 69, 89]:
        t2 = t2s[index_t2]
        aMs_rescale = aMs /((1+t2)/2) *np.power((1+t2**order)/2, 1/order)
        ax.plot(aMs_rescale, nonlin_results[5,index_t2,:], label='$T_2/T_1={t2:.2}$'.format(t2=t2), linewidth=linewidth)
    # index_t2 = 7
    # ax.plot(aMs, nonlin_Whit[5,index_t2,:], label='$T_2/T_1={t2:.2}$'.format(t2=t2s[index_t2]))
    # ax.plot(lin_data[:,0], lin_data[:,3], 'k', label='linear', linewidth=linewidth)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(r"$P/((k_\mathrm{B}T_1)^2/h)$") # , '$zT$'
    ax.legend(fontsize=28)
    ax.set_ylim([0,ylim])
    ax.set_xlim([0,xlim])


def rescale_plot_e0e1(order=1, xlim=100, ylim=40, linewidth=2, xlabel=r"$\alpha'M_0$"):
    fig, ax = plt.subplots(figsize=(17, 10))
    lines = []
    legend_t2s = []
    color_cyc = plt.rcParams['axes.prop_cycle'].by_key()['color']
    i = 0
    for index_t2 in [0, 14, 29, 59, 98]:
        t2 = t2s[index_t2]
        rescale = 1 # np.power((1+t2**order)/2, 1/order)
        e0 = nonlin_results[0,index_t2,:] /rescale
        e1 = nonlin_results[1,index_t2,:] /rescale
        e0line, = ax.plot(aMs, e0, linewidth=linewidth, color=color_cyc[i])
        e1line, = ax.plot(aMs, e1, linewidth=linewidth, color=color_cyc[i])
        i += 1
        lines.append((e0line, e1line))
        legend_t2s.append('$T_2/T_1={t2:.2}$'.format(t2=t2))
    e0line, = ax.plot(lin_data[:,0], lin_data[:,1], 'k', linewidth=linewidth)
    e1line, = ax.plot(lin_data[:,0], lin_data[:,2], 'k', linewidth=linewidth)
    lines.append((e0line, e1line))
    legend_t2s.append('linear')
    ax.set_xlabel(xlabel)
    ax.set_ylabel("$\epsilon'$") # r"$P/((k_\mathrm{B}T_1)^2/h)$"
    ax.legend(lines, legend_t2s, fontsize=28)
    ax.set_ylim([0,ylim])
    ax.set_xlim([0,xlim])