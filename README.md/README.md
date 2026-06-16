# Motivation (what , why and how?)

# Project structure

## Option pricing with the Black-Scholes formula

### Assumptions:
- The option can only be exercised at maturity.
- No dividends are paid.
- Markets are fristionless (no transaction costs, taxes or restrictions).
- Risk-free rate and the volatility of the underlying asset are constant.
- Returns are normally distributed.
- There are no arbitrage opportunities in the market.
- The underlying asset's price follows GBM.

## Greeks results on the orginial trial

Values:
- S = 150
- K = 130
- T = 1
- r = 0.04
- sigma = 0.03

Results:
Call Delta: 1.0
Put Delta: 0.0
Gamma: 2.2718750455547073e-137
Vega: 1.5335156557494274e-136
Call Theta: -0.013687959133128988
Put Theta: -5.63715087810405e-139
Call Rho: 1.2490262708980202
Put Rho: -6.067835327904063e-138


### How to run it

# Current project progress:

## Seting up

- [x] Create repository
- [x] Set up project structure

## Buidling the python models

- [x] Build Black-Scholes model
- [ ] Greeks
- [ ] Monte Carlo simulation
- [ ] Binomial Tree model

## Analytics, documentation and READ.ME

- [X] Create a READ.ME doc
- [ ] Add Greeks section in theory paper
- [ ] Add Monte Carlo simulation in the theory paper
- [ ] Add Binomial Tree section to theory paper
- [ ] Import the option price theory paper
- [ ] Explain on READ.ME the aim and functionality of each model
- [ ] Explain the results of the Greeks trials
- [ ] Write the requirements down on requirements.txt

# Skills demonstrated