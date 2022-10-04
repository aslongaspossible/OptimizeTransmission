import numpy as np
from scipy import integrate

def fermi_dist(energy:float, chemical_potential=0., temperature=1.) -> float:
    """返回费米分布。

    Args:
        energy: 能量，单位是 kBT1。
        chemical_potential: 化学势，单位是 kBT1。
        temperature: 温度，单位是 T1。
    """
    energy_bar = energy -chemical_potential
    esign = np.sign(energy_bar) # 为了保证不会数值溢出
    ebar = np.exp(-np.abs(energy_bar)/temperature)
    return np.maximum(-esign, ebar) /(1+ebar)


def current_kernal(energy, dmu, t2):
    """电流的积分核。

    Args:
        energy: 能量。
        dmu: 两边化学势的差，对应电压。
        t2: `t2/t1`，即以 t1 为单位的温度 t2。
    """
    return fermi_dist(energy)-fermi_dist(energy, dmu, t2)

def current(x1, x2, dmu, t2):
    """电流。

    Args:
        x1: 透射窗口的起始位置。
        x2: 透射窗口的结束位置。
        dmu: 两边化学势的差，对应电压。
        t2: `t2/t1`，即以 t1 为单位的温度 t2。
    """
    return integrate.quad(current_kernal, x1, x2, args=(dmu, t2))[0]


def heat_kernal(energy, dmu, t2):
    """电子贡献的热流的积分核。

    Args:
        energy: 能量。
        dmu: 两边化学势的差，对应电压。
        t2: `t2/t1`，即以 t1 为单位的温度 t2。
    """
    return energy*current_kernal(energy, dmu, t2)

def heat(x1, x2, dmu, t2, alphaM):
    """总热流。

    Args:
        x1: 透射窗口的起始位置。
        x2: 透射窗口的结束位置。
        dmu: 两边化学势的差，对应电压。
        t2: `t2/t1`，即以 t1 为单位的温度 t2。
        alphaM: 对应了线性版本中的 `alpha'M0`。
    """
    # TODO 这里到底应该取什么样的 alpha(T) 呢？
    return integrate.quad(heat_kernal, x1, x2, args=(dmu, t2))[0] + (1-t2) /alphaM *(1+t2)/2

