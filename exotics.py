import numpy as np


class GeometricBrownianMotion:

    def simulate_path(self, S, mu, sigma, dt, T):
        prev_price = S
        prices = []
        step = 0
        while step < T:
            ds = prev_price*mu*dt + prev_price*sigma*np.random.randn()*np.sqrt(dt)
            prev_price = prev_price+ds
            prices.append((prev_price))
            step += dt
        return prices

    def __init__(self, S, mu, sigma, dt, T):
        self.simulated_path = self.simulate_path(S, mu, sigma, dt, T)


class MonteCarloCall:

    def __init__(self):
        pass


class MonteCarloPut:

    def __init__(self):
        pass


class MonteCarloBinaryCall:

    def simulate_price(self, strike, payout, n, r, S, mu, sigma, dt, T):
        payouts = []
        for i in range(0, n):
            GBM = GeometricBrownianMotion(S, mu, sigma, dt, T)
            if(GBM.simulated_path[-1] >= strike):
                payouts.append(payout*np.exp(-r*T))
            else:
                payouts.append(0)
        return np.average(payouts)


    def __init__(self, strike, payout, n, r, S, mu, sigma, dt, T):
        self.price = self.simulate_price(strike, payout, n, r,  S, mu, sigma, dt, T)


class MonteCarloBinaryPut:

    def simulate_price(self, strike, payout, n, r, S, mu, sigma, dt, T):
        payouts = []
        for i in range(0, n):
            GBM = GeometricBrownianMotion(S, mu, sigma, dt, T)
            if(GBM.simulated_path[-1] <= strike):
                payouts.append(payout*np.exp(-r*T))
            else:
                payouts.append(0)
        return np.average(payouts)


    def __init__(self, strike, payout, n, r, S, mu, sigma, dt, T):
        self.price = self.simulate_price(strike, payout, n, r, S, mu, sigma, dt, T)
