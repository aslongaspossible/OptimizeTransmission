import numpy as np
import collections
from scipy import optimize
from . import current
from generator import efficiency, eta2zT


class Solver:
    def __init__(self, equation):
        self.equation = equation

    def solve4aM(self, t2, aM, guess):
        solx = optimize.root(self.equation, guess, args=(t2, aM)).x
        x1, x2 = solx
        dmu = x1 *(1-t2)
        eta = efficiency(x1, x2, dmu, t2, aM)
        power = dmu * current(x1, x2, dmu, t2)
        x1 -= dmu/2
        x2 -= dmu/2
        zT1 = eta2zT(eta, t2)
        return [np.array([x1, x2, dmu, eta, zT1, power]), solx]

    def solve4t2(self, t2, start_aM, aMs, guess0):
        result, guess0 = self.solve4aM(t2, aMs[start_aM], guess0)
        tot_results = collections.deque([result])
        guess = guess0
        for alphaM in aMs[start_aM+1:]:
            result, guess = self.solve4aM(t2, alphaM, guess)
            tot_results.append(result)
        guess = guess0
        for alphaM in aMs[start_aM-1::-1]:
            result, guess = self.solve4aM(t2, alphaM, guess)
            tot_results.appendleft(result) # 特别注意：这次是从最开始加
        print('t2={t2:.2}, '.format(t2=t2), tot_results[0])
        return [np.column_stack(tot_results), guess0]

    def solve4nonlin(self, t2s, aMs, start_t2=30, start_aM=30):
        """对一系列 T2/T1 和 aM 解方程"""
        result, guess0 = self.solve4t2(t2s[start_t2], start_aM, aMs, [2.2, 6.])
        tot_results = collections.deque([result])
        guess = guess0
        for t2 in t2s[start_t2+1:]:
            result, guess = self.solve4t2(t2, start_aM, aMs, guess)
            # print(result.shape)
            tot_results.append(result)
        # print(len(results))
        guess = guess0
        for t2 in t2s[start_t2-1::-1]:
            result, guess = self.solve4t2(t2, start_aM, aMs, guess)
            tot_results.appendleft(result)
        return np.stack(tot_results, axis=1)