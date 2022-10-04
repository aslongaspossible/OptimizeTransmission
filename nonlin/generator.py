
from scipy import integrate
from . import current, heat, fermi_dist


def efficiency(x1, x2, dmu, t2, alphaM):
    """温差发电机的效率。
    
    Args:
        x1: 透射窗口的起始位置。
        x2: 透射窗口的结束位置。
        dmu: 两边化学势的差，对应电压。
        t2: `t2/t1`，即以 t1 为单位的温度 t2。
        alphaM: 对应了线性版本中的 `alpha'M0`。
    """
    return dmu*current(x1, x2, dmu, t2) /heat(x1, x2, dmu, t2, alphaM)

def eta2zT(eta, t2):
    """已知温差发电机的效率，求等效的 zT。
    
    Args:
        eta: 温差发电机的效率。
        t2: `t2/t1`，即以 t1 为单位的温度 t2。
    """
    return ((1-(1-eta)*t2) /(1-t2-eta))**2-1


def eq_nonlin(x, t2, alphaM):
    """非线性输运热机的方程组。
    
    Args:
        x: 要求的解，包括：
            x1: 透射窗口的起始位置。
            x2: 透射窗口的结束位置。
        t2: `t2/t1`，即以 t1 为单位的温度 t2。
        alphaM: 对应了线性版本中的 `alpha'M0`。
    """
    x1, x2 = x
    dmu = x1 *(1-t2)
    currentI =  current(x1, x2, dmu, t2) # 电流
    heatJ = heat(x1, x2, dmu, t2, alphaM) # 热流
    def int_kern(energy, dmu, t2):
        f2 = fermi_dist(energy, dmu, t2)
        return f2*(1-f2)
    int1 = integrate.quad(int_kern, x1, x2, args=(dmu,t2))[0]
    int2 = integrate.quad(
        lambda energy, dmu, t2: energy*int_kern(energy, dmu, t2),
        x1, x2, args=(dmu,t2)
    )[0]
    return [
        heatJ - currentI*x2,
        heatJ*(currentI*t2-int1*dmu) + currentI*int2*dmu
    ]