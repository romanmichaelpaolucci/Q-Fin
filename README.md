# Q-Fin
A mathematical finance Python library

# Time Value of Money

# Bond Pricing

# Option Pricing

### <a href="https://medium.com/swlh/deriving-the-black-scholes-model-5e518c65d0bc"> Black-Scholes Pricing</a>
Theoretical options pricing for non-dividend paying stocks is available via the BlackScholesCall and BlackScholesPut classes.

```Python
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

# Simulation Pricing

### <a href="https://medium.com/swlh/python-for-pricing-exotics-3a2bfab5ff66"> Exotic Options </a>
Simulation pricing for exotic options is available under the assumptions of Geometric Brownian motion.

#### Binary Options
```Python
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
