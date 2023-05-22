import numpy as np


def const(_:float) -> float:
    """Constant density of modes."""
    return 1.

def ti(x:np.ndarray, mu:float, vw:float, gap:float, cw:float) -> np.ndarray:
    """DoM of TIs.
    
    Args:
        x: E/(kBT)
        mu: Energy of the center of gap.
        vw: Width of valence band.
        cw: Width of conducting band.
    """
    tv = -gap/2 +mu # top of valence band
    bc = gap/2 +mu # bottom of conducting band
    bv = tv -vw # bottom of valence band
    tc = bc +cw # top of conducting band
    bulk = np.logical_or(np.logical_and(x>bv, x<tv), np.logical_and(x>bc, x<tc))
    edge = np.logical_and(x>bv, x<tc)
    return (edge*2+bulk*2)*2

def basin(x:np.ndarray, mu:float, gap:float) -> np.ndarray:
    tv = -gap/2 +mu # top of valence band
    bc = gap/2 +mu # bottom of conducting band
    low = np.logical_and(x>tv, x<bc)
    return (4-2*low)*2


def boxcar(x, x1, x2):
    x1, x2 = sorted([x1, x2])
    return np.where(np.logical_or(x<x1, x>x2), 0, 1)

def trapezoid(x, x1, x2):
    x1, x2 = sorted([x1, x2])
    d = (x2-x1)/4
    return np.piecewise(
        x,
        [
            x < x1+d,
            x > x2-d,
            np.logical_or(x<x1-d, x>x2+d),
        ], # the order matters
        [
            lambda x: (x-x1+d)/2/d,
            lambda x: (x2+d-x)/2/d,
            0.,
            1.
        ]
    )
