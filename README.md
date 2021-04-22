# Q-Fin
A mathematical finance Python library

## Installation
https://pypi.org/project/QFin/
```
pip install qfin
```

# Time Value of Money

# Bond Pricing

# Option Pricing

### <a href="https://medium.com/swlh/deriving-the-black-scholes-model-5e518c65d0bc"> Black-Scholes Pricing</a>
Theoretical options pricing for non-dividend paying stocks is available via the BlackScholesCall and BlackScholesPut classes.

```Python
from qfin.options import BlackScholesCall
from qfin.options import BlackScholesPut
# 100 - initial underlying asset price
# .3 - asset underlying volatility
# 100 - option strike price
# 1 - time to maturity (annum)
# .01 - risk free rate of interest
euro_call = BlackScholesCall(100, .3, 100, 1, .01)
euro_put = BlackScholesPut(100, .3, 100, 1, .01)
```

```Python
print('Call price: ', euro_call.price)
print('Put price: ', euro_put.price)
```

```
Call price:  12.361726191532611
Put price:  11.366709566449416
```

### Option Greeks
First-order and some second-order partial derivatives of the Black-Scholes pricing model are available.

#### Delta
First-order partial derivative with respect to the underlying asset price.
```Python
print('Call delta: ', euro_call.delta)
print('Put delta: ', euro_put.delta)
```
```
Call delta:  0.5596176923702425
Put delta:  -0.4403823076297575
```

#### Gamma
Second-order partial derivative with respect to the underlying asset price.
```Python
print('Call gamma: ', euro_call.gamma)
print('Put gamma: ', euro_put.gamma)
```
```
Call gamma:  0.018653923079008084
Put gamma:  0.018653923079008084
```

#### Vega
First-order partial derivative with respect to the underlying asset volatility.
```Python
print('Call vega: ', euro_call.vega)
print('Put vega: ', euro_put.vega)
```
```
Call vega:  39.447933090788894
Put vega:  39.447933090788894
```

#### Theta
First-order partial derivative with respect to the time to maturity.
```Python
print('Call theta: ', euro_call.theta)
print('Put theta: ', euro_put.theta)
```
```
Call theta:  -6.35319039407325
Put theta:  -5.363140560324083
```

# Stochastic Processes
Simulating asset paths is available using common stochastic processes.

### <a href="https://towardsdatascience.com/geometric-brownian-motion-559e25382a55"> Geometric Brownian motion </a>
```Python
from qfin.simulations import GeometricBrownianMotion
# 100 - initial underlying asset price
# 0 - underlying asset drift (mu)
# .3 - underlying asset volatility
# 1/52 - time steps (dt)
# 1 - time to maturity (annum)
gbm = GeometricBrownianMotion(100, 0, .3, 1/52, 1)
```

```Python
print(gbm.simulated_path)
```

```
[107.0025048205179, 104.82320056538235, 102.53591127422398, 100.20213816642244, 102.04283245358256, 97.75115579923988, 95.19613943526382, 96.9876745495834, 97.46055174410736, 103.93032659279226, 107.36331603194304, 108.95104494118915, 112.42823319947456, 109.06981862825943, 109.10124426285238, 114.71465058375804, 120.00234814086286, 116.91730159923688, 118.67452601825876, 117.89233466917202, 118.93541257993591, 124.36106523035058, 121.26088015675688, 120.53641952983601, 113.73881043255554, 114.91724168548876, 112.94192281337791, 113.55773877160591, 107.49491796151044, 108.0715118831013, 113.01893111071472, 110.39204535739405, 108.63917240906524, 105.8520395233433, 116.2907247951675, 114.07340779267213, 111.06821275009212, 109.65530380775077, 105.78971667172465, 97.75385009989282, 97.84501925249452, 101.90695475825825, 106.0493833583297, 105.48266575656817, 106.62375752876223, 112.39829297429974, 111.22855058562658, 109.89796974828265, 112.78068777325248, 117.80550869036715, 118.4680557054793, 114.33258212280838]
```

# Simulation Pricing

### <a href="https://medium.com/swlh/python-for-pricing-exotics-3a2bfab5ff66"> Exotic Options </a>
Simulation pricing for exotic options is available under the assumptions associated with Geometric Brownian motion.

#### Vanilla Options
```Python
from qfin.simulations import MonteCarloCall
from qfin.simulations import MonteCarloPut
# 100 - strike price
# 1000 - number of simulated price paths
# .01 - risk free rate of interest
# 100 - initial underlying asset price
# 0 - underlying asset drift (mu)
# .3 - underlying asset volatility
# 1/52 - time steps (dt)
# 1 - time to maturity (annum)
call_option = MonteCarloCall(100, 1000, .01, 100, 0, .3, 1/52, 1)
put_option = MonteCarloCall(100, 1000, .01, 100, 0, .3, 1/52, 1)
```

```Python
print(call_option.price)
print(put_option.price)
```

```
12.73812121792851
12.304109267761028
```

#### Binary Options
```Python
from qfin.simulations import MonteCarloBinaryCall
from qfin.simulations import MonteCarloBinaryPut
# 100 - strike price
# 50 - binary option payout
# 1000 - number of simulated price paths
# .01 - risk free rate of interest
# 100 - initial underlying asset price
# 0 - underlying asset drift (mu)
# .3 - underlying asset volatility 
# 1/52 - time steps (dt)
# 1 - time to maturity (annum)
binary_call = MonteCarloBinaryCall(100, 50, 1000, .01, 100, 0, .3, 1/52, 1)
binary_put = MonteCarloBinaryPut(100, 50, 1000, .01, 100, 0, .3, 1/52, 1)
```

```Python
print(binary_call.price)
print(binary_put.price)
```

```
22.42462873441866
27.869902820039087
```
# Futures Pricing
