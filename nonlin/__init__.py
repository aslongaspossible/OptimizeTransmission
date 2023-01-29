import numpy as np
from scipy import integrate

def fermi_dist(energy:float, chemical_potential=0., temperature=1.) -> float:
    """Return fermi distribution.

    Args:
        energy: in the unit of kBT1, choose mu1 as energy zero.
        chemical_potential: in the unit of kBT1.
        temperature: in the unit of T1.
    """
    energy_bar = energy -chemical_potential
    esign = np.sign(energy_bar) # to avoid float overflow
    ebar = np.exp(-np.abs(energy_bar)/temperature)
    return np.maximum(-esign, ebar) /(1+ebar)


def current_kernal(energy, dmu, t2):
    """Intergral kernal of electrical current.

    Args:
        energy: in the unit of kBT1, choose mu1 as energy zero.
        dmu: mu2-mu1=eU in the unit of kBT1, where U is the voltage.
        t2: in the unit of T1.
    """
    return fermi_dist(energy)-fermi_dist(energy, dmu, t2)

def current(x1, x2, dmu, t2):
    """Electrical current /N, in the unit of e/h.

    Args:
        x1: start point of optimal transport window.
        x2: end point of optimal transport window.
        dmu: mu2-mu1=eU in the unit of kBT1, where U is the voltage.
        t2: in the unit of T1.
    """
    return integrate.quad(current_kernal, x1, x2, args=(dmu, t2))[0]


def heat_kernal(energy, dmu, t2):
    """Intergral kernal of electron heat current.

    Args:
        energy: in the unit of kBT1, choose mu1 as energy zero.
        dmu: mu2-mu1=eU in the unit of kBT1, where e is elementary charge and U the voltage.
        t2: in the unit of T1.
    """
    return energy*current_kernal(energy, dmu, t2)

def heat(x1, x2, dmu, t2, boverN):
    """(Je + Jph)/N, total heat current, in the unit of kBT1/h.

    Args:
        x1: start point of optimal transport window.
        x2: end point of optimal transport window.
        dmu: mu2-mu1=eU in the unit of kBT1, where e is elementary charge and U the voltage.
        t2: in the unit of T1.
        boverN: beta/N.
    """
    return integrate.quad(heat_kernal, x1, x2, args=(dmu, t2))[0] + boverN*(1-t2) *(1+t2)/2

