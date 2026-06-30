import numpy as np
from black_scholes import call_price, put_price

def terminal_stock_price(S, sigma, T, N):
    dt = T/N
    u = np.exp(sigma * np.sqrt(dt))
    d = 1/u
    p = (np.exp(r*dt)-d)/(u-d)
    
    j=np.arange(N+1)
    S_T = S * u ** j * d ** (N-j)

    return S_T

def binomial_tree_price(S, K, r, sigma, T, N, option_type='call'):

    S_T=terminal_stock_price(S, sigma, T, N)
    dt = T/N
    u = np.exp(sigma * np.sqrt(dt))
    d = 1/u
    p = (np.exp(r*dt)-d)/(u-d)

    if option_type=='call':
        payoff=np.maximum(S_T-K, 0)
    elif option_type=='put':
        payoff=np.maximum(K-S_T, 0)
    else:
        raise ValueError("option type must be 'call' or 'put'")

    for i in range (N):
        payoff = np.exp(-r*dt) * (p * payoff[1:] + (1-p) * payoff[:-1])

    return payoff[0]

if __name__ == "__main__":
    S=200
    K=150
    r=0.07
    sigma=0.18
    T=1
    N=3

    bt_call = binomial_tree_price(S, K, r, sigma, T, N, option_type='call')
    bt_put = binomial_tree_price(S, K, r, sigma, T, N, option_type='put')

    bs_call = call_price(S, K, r, sigma, T)
    bs_put = put_price(S, K, r, sigma, T)

    print("Binomial Tree VS Black-Scholes model:")
    print("------------------")
    print(f"BT - Call: {bt_call:.2f} | BS: {bs_call:.2f} | Diff: {abs(bt_call - bs_call):.4f}")
    print(f"BT - Put: {bt_put:.2f} | BS: {bs_put:.2f} | Diff: {abs(bt_put - bs_put):.4f}")
    