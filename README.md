# Q-Fin
A mathematical finance Python library

# Time Value of Money

# Bond Pricing

# Option Pricing

### <a href="https://medium.com/swlh/deriving-the-black-scholes-model-5e518c65d0bc"> Black-Scholes Pricing</a>
Theoretical options pricing for non-dividend paying stocks is available via the BlackScholesCall and BlackScholesPut classes.

```Python
# 100 - initial asset price
# .3 - asset volatility
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

# Exotics Pricing

# Futures Pricing
