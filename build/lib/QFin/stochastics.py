from abc import ABC, abstractmethod
from scipy.stats import norm
import numpy as np

# Abstract class framework for a stochastic process
class StochasticModel:

    @abstractmethod
    # Risk neutral pricing kernel
    def vanilla_pricing(self, F0, X, T, op_type="CALL"):
        pass

    # Calibration is conducted via an inputted vol surface and the vanilla pricing function
    def calibrate(self, impl_vol, T, op_type="CALL"):
        pass

    # simulation is conducted after calibration of params to price exotics
    @abstractmethod
    def simulate(self):
        pass

    def __init__(self, params) -> None:
        self.params = params


class ArithmeticBrownianMotion(StochasticModel):

    # closed form vanilla euro option pricing
    def vanilla_pricing(self, F0, X, T, op_type="CALL"):
        # return closed-form Bachelier call
        if op_type == "CALL":
            return (F0 - X)*(norm.cdf((F0 - X)/(self.params[0]*np.sqrt(T)))) + self.params[0]*np.sqrt(T)*(norm.pdf((F0 - X)/(self.params[0]*np.sqrt(T))))
        # use call-put parity for put price
        elif op_type == "PUT":
            return self.vanilla_pricing(F0, X, T) - F0 + X
        else:
            return "Option type must be CALL/PUT"
        
    # simulating paths of arithmetic Brownian motion
    def simulate(self, F0, n, dt, T):
        paths = []
        for i in range(n):
            # n simulations
            ttm = T
            path = [F0]
            # while the step is greator than zero diffuse the process
            while ttm-dt > 0:
                path.append(path[-1] + self.params[0]*np.random.randn()*np.sqrt(dt))
                ttm -= dt
            # final time increment
            if dt > 0:
                path.append(path[-1] + self.params[0]*np.random.randn()*np.sqrt(dt))
            # append the path
            paths.append(path)

        # store paths and path characteristics
        self.path_characteristics = (paths, n, dt, T)

        # return paths and path characteristics
        return (paths, n, dt, T)

    # Calibration cannot be conducted due to flat volatility surface
    def __init__(self, params) -> None:
        super().__init__(params)