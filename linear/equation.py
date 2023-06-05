import numpy as np
from scipy import integrate
from scipy.optimize import root
from collections import deque
from dom import const as constdom


def kernel(x:float, j:int, dom) -> float:
    """Return $e^xx^jM(x)/(1+e^x)^2$.

    Args:
        x: E/(kBT)
        dom: density of modes
    """
    ex = np.exp(-abs(x)) # To avoid overflow.
    return x**j *dom(x) * ex/(1+ex)**2

def I(x1, x2, j, dom=constdom) -> float:
    """Return $I_j$.
    
    Args:
        x1: start position of transport window
        x2: end position of transport window
        dom: density of modes
    """
    return integrate.quad(kernel, x1, x2, args=(j,dom))[0]


def eq(x:list, beta:float, dom) -> list[float]:
    """Equations"""
    numerator = I(x[0], x[1], 2, dom) +beta
    # Avoid division
    return [
        (x[0]+x[1]) *I(x[0],x[1],1,dom) -2*numerator,
        x[0]*x[1]*I(x[0],x[1],0,dom) -numerator
    ]

def jac(x:list[float], _, dom) -> np.ndarray:
    """Jacobian
    
    Args:
        _: Should be beta, but Jacobian is independent of beta.
    """
    int1 = I(x[0], x[1], 1, dom)
    int0 = I(x[0], x[1], 0, dom)
    sumx = x[0] + x[1]
    prodx = x[0]*x[1]
    k2x0 = kernel(x[0],2,dom)
    k2x1 = kernel(x[1],2,dom)
    return np.array([
        [
            int1 -sumx*kernel(x[0],1,dom) +2*k2x0,
            int1 +sumx*kernel(x[1],1,dom) -2*k2x1
        ],
        [
            x[1]*int0 -prodx*kernel(x[0],0,dom) +k2x0,
            x[0]*int0 +prodx*kernel(x[1],0,dom) -k2x1
        ]
    ])


def solve_eq(guess:list, beta:float, dom) -> list[float]:
    """Solve for x and zT
    
    Args:
        guess: A guess for result
        dom: density of modes
        
    Returns:
        x1: start position of transport window
        x2: end position of transport window
        zT: thermoelectric figure of merit
        pf: power factor in the unit of $k_B^2/h$
        seebeck: Seebeck coefficient in the unit of $k_B/e$
    """
    x1, x2 = root(eq, guess, args=(beta,dom), jac=jac).x
    prodx = x1*x2
    seebeck = 2*prodx /(x1+x2)
    return [x1, x2,
        4*prodx /(x1-x2)**2,
        seebeck**2 *I(x1,x2,0,dom),
        seebeck
    ]


def solve4beta(dom, beta_range=np.logspace(-3,3,num=301), guess=[1.6, 8.9]):
    """Solve optimal transport window for certain density of modes and beta parameters.
    
    Args:
        dom: Density of modes.
        guess: A guess for beta=0.
        
    Returns:
        result_total: Stack of results. Each result contains:
            1/beta: equation parameter
            x1: start position of transport window
            x2: end position of transport window
            zT: figure of merit
            pf: power factor in the unit of $k_B^2/h$
            seebeck: Seebeck coefficient in the unit of $k_B/e$
        """
    start_index = int(np.where(np.isclose(beta_range, 1.))[0])
    beta = beta_range[start_index]
    print("beta start at",beta)
    result = solve_eq(guess, beta, dom)
    result_total = deque([[1/beta]+result])
    guess0 = [result[0], result[1]]
    guess = guess0
    for beta in beta_range[start_index+1:]:
        result = solve_eq(guess, beta, dom)
        result_total.appendleft([1/beta]+result)
        guess = [result[0], result[1]]
    guess = guess0
    for beta in beta_range[start_index-1::-1]:
        result = solve_eq(guess, beta, dom)
        result_total.append([1/beta]+result)
        guess = [result[0], result[1]]
    # print(result_total)
    return np.vstack(result_total)


def kappa_e(x1, x2, dom):
    return (I(x1,x2,2,dom) - I(x1,x2,1,dom)**2 / I(x1,x2,0,dom))

def sigma_seebeck_zT(x1, x2, beta, dom=constdom):
    """
    Args:
      x1, x2: bounds of the integral (support of dom)
      dom: Density of Modes / number of modes
      beta: lattice heat conductance
    
    Returns:
      electrical conductance
      Seebeck coefficient
      zT
    """
    i0 = I(x1,x2,0,dom)
    i1 = I(x1,x2,1,dom)
    i12 = i1**2
    return [
        i0,
        np.divide(i1, i0),
        np.divide(i12, ((I(x1,x2,2,dom)+beta)*i0-i12))
        ]
