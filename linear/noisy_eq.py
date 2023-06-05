from collections import deque
import numpy as np
from scipy.optimize import root
from scipy import integrate
from equation import I


H2 = I(-np.inf, np.inf, 2)
H0 = I(-np.inf, np.inf, 0)

def noisy_eq(x, beta, noise):
    noise_rate = noise / (1-noise)
    numerator = noise_rate * H2 + I(x[0],x[1],2) + beta / (1-noise)
    return [
        (x[0]+x[1]) *I(x[0],x[1],1) -2*numerator,
        x[0]*x[1]*(I(x[0],x[1],0) + H0*noise_rate) -numerator
    ]

def solve_noisy_eq(guess:list, beta:float, noise):
    """Solve for x and zT
    
    Args:
        guess: A guess for result
        
    Returns:
        x1: start position of transport window
        x2: end position of transport window
        zT: thermoelectric figure of merit
        pf: power factor in the unit of $k_B^2/h$
        seebeck: Seebeck coefficient in the unit of $k_B/e$
        sigma: electrical conductance
        heat conductance
    """
    x1, x2 = root(noisy_eq, guess, args=(beta,noise)).x
    prodx = x1 * x2
    zT = 4*prodx /(x1-x2)**2
    seebeck = 2*prodx /(x1+x2)
    sigma = (1-noise) * I(x1,x2,0) + noise * H0
    power_factor = seebeck**2 * sigma
    return [x1, x2,
        zT ,
        power_factor,
        seebeck,
        sigma,
        power_factor / zT
    ]

def solve_noise4beta(noise, beta_range=np.logspace(-3,3,num=301), guess=[1.6, 8.9]):
    """Solve for x and zT
    
        
    Returns: n*8 array, each column is:
        1/beta: reverse of phonon heat conductance
        x1: start position of transport window
        x2: end position of transport window
        zT: thermoelectric figure of merit
        pf: power factor in the unit of $k_B^2/h$
        seebeck: Seebeck coefficient in the unit of $k_B/e$
        sigma: electrical conductance
        kappa: heat conductance
    """
    start_index = int(np.where(np.isclose(beta_range, 1.))[0])
    beta = beta_range[start_index]
    print("beta start at",beta)
    result = solve_noisy_eq(guess, beta, noise)
    result_total = deque([[1/beta]+result])
    guess0 = [result[0], result[1]]
    guess = guess0
    for beta in beta_range[start_index+1:]:
        result = solve_noisy_eq(guess, beta, noise)
        result_total.appendleft([1/beta]+result)
        guess = [result[0], result[1]]
    guess = guess0
    for beta in beta_range[start_index-1::-1]:
        result = solve_noisy_eq(guess, beta, noise)
        result_total.append([1/beta]+result)
        guess = [result[0], result[1]]
    # print(result_total)
    return np.vstack(result_total)
