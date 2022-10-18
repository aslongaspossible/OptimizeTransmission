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