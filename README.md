# Q-Fin
A Python library for mathematical finance.

## Installation
https://pypi.org/project/QFin/
```
pip install qfin
```

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

### <a href="https://towardsdatascience.com/geometric-brownian-motion-559e25382a55"> Geometric Brownian Motion </a>
Standard model for implementing geometric Brownian motion.
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

### <a href="https://towardsdatascience.com/stochastic-volatility-pricing-in-python-931f4b03d793"> Stochastic Variance Process </a>
Stochastic volatility model based on Heston's paper (1993).
```Python
from qfin.simulations import StochasticVarianceModel
# 100 - initial underlying asset price
# 0 - underlying asset drift (mu)
# .01 - risk free rate of interest
# .05 - continuous dividend
# 2 - rate in which variance reverts to the implied long run variance
# .25 - implied long run variance as time tends to infinity
# -.7 - correlation of motion generated
# .3 - Variance's volatility
# 1/52 - time steps (dt)
# 1 - time to maturity (annum)
svm = StochasticVarianceModel(100, 0, .01, .05, 2, .25, -.7, .3, .09, 1/52, 1)
```

```Python
print(svm.simulated_path)
```

```
[98.21311553503577, 100.4491317019877, 89.78475515902066, 89.0169762497475, 90.70468848525869, 86.00821802256675, 80.74984494892573, 89.05033807013137, 88.51410029337134, 78.69736798230346, 81.90948751054125, 83.02502248913251, 83.46375102829755, 85.39018282900138, 78.97401642238059, 78.93505221741903, 81.33268688455111, 85.12156706038515, 79.6351983987908, 84.2375291273571, 82.80206517176038, 89.63659376223292, 89.22438477640516, 89.13899271995662, 94.60123239511816, 91.200165507022, 96.0578905115345, 87.45399399599378, 97.908745925816, 97.93068975065052, 103.32091104292813, 110.58066464778392, 105.21520242908348, 99.4655106985056, 106.74882010453683, 112.0058519886151, 110.20930861932342, 105.11835510815085, 113.59852610881678, 107.13315204738092, 108.36549026977205, 113.49809943785571, 122.67910031073885, 137.70966794451425, 146.13877267735612, 132.9973784430374, 129.75750117504984, 128.7467891695649, 127.13115959080305, 130.47967713110302, 129.84273088908265, 129.6411527208744]
```

# Simulation Pricing

### <a href="https://medium.com/swlh/python-for-pricing-exotics-3a2bfab5ff66"> Exotic Options </a>
Simulation pricing for exotic options is available under the assumptions associated with the respective stochastic processes.  Geometric Brownian motion is the base underlying stochastic process used in each Monte Carlo simulation.  However, should additional parameters be provided, the appropriate stochastic process will be used to generate each sample path.

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
# These additional parameters will generate a Monte Carlo price based on a stochastic volatility process
# 2 - rate in which variance reverts to the implied long run variance
# .25 - implied long run variance as time tends to infinity
# -.5 - correlation of motion generated
# .02 - continuous dividend
# .3 - Variance's volatility
put_option = MonteCarloPut(100, 1000, .01, 100, 0, .3, 1/52, 1, 2, .25, -.5, .02, .3)
```

```Python
print(call_option.price)
print(put_option.price)
```

```
12.73812121792851
23.195814963576286
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

#### Barrier Options
```Python
from qfin.simulations import MonteCarloBarrierCall
from qfin.simulations import MonteCarloBarrierPut
# 100 - strike price
# 50 - binary option payout
# 1000 - number of simulated price paths
# .01 - risk free rate of interest
# 100 - initial underlying asset price
# 0 - underlying asset drift (mu)
# .3 - underlying asset volatility
# 1/52 - time steps (dt)
# 1 - time to maturity (annum)
# True/False - Barrier is Up or Down
# True/False - Barrier is In or Out
barrier_call = MonteCarloBarrierCall(100, 1000, 150, .01, 100, 0, .3, 1/52, 1, up=True, out=True)
barrier_put = MonteCarloBarrierCall(100, 1000, 95, .01, 100, 0, .3, 1/52, 1, up=False, out=False)
```

```Python
print(binary_call.price)
print(binary_put.price)
```

```
4.895841997908933
5.565856754630819
```

#### Asian Options
```Python
from qfin.simulations import MonteCarloAsianCall
from qfin.simulations import MonteCarloAsianPut
# 100 - strike price
# 1000 - number of simulated price paths
# .01 - risk free rate of interest
# 100 - initial underlying asset price
# 0 - underlying asset drift (mu)
# .3 - underlying asset volatility
# 1/52 - time steps (dt)
# 1 - time to maturity (annum)
asian_call = MonteCarloAsianCall(100, 1000, .01, 100, 0, .3, 1/52, 1)
asian_put = MonteCarloAsianPut(100, 1000, .01, 100, 0, .3, 1/52, 1)
```

```Python
print(asian_call.price)
print(asian_put.price)
```

```
6.688201154529573
7.123274528125894
```

#### Extendible Options
```Python
from qfin.simulations import MonteCarloExtendibleCall
from qfin.simulations import MontecarloExtendiblePut
# 100 - strike price
# 1000 - number of simulated price paths
# .01 - risk free rate of interest
# 100 - initial underlying asset price
# 0 - underlying asset drift (mu)
# .3 - underlying asset volatility
# 1/52 - time steps (dt)
# 1 - time to maturity (annum)
# .5 - extension if out of the money at expiration
extendible_call = MonteCarloExtendibleCall(100, 1000, .01, 100, 0, .3, 1/52, 1, .5)
extendible_put = MonteCarloExtendiblePut(100, 1000, .01, 100, 0, .3, 1/52, 1, .5)
```

```Python
print(extendible_call.price)
print(extendible_put.price)
```

```
13.60274931789973
13.20330578685724
```


# Futures Pricing
