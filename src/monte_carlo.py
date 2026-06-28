import numpy as np
from black_scholes import call_price, put_price

# Defining how we price the asset
def simulate_terminal_prices(S, K, r, sigma, T, n_simulations=1000_000, seed=42):
    np.random.seed(seed)
    Z=np.random.standard_normal(n_simulations)
    S_T=S*np.exp((r-0.5*sigma**2)*T+sigma*np.sqrt(T)*Z)

    return S_T

# Creating the payoff and pricing function (through MC simulation)
def monte_carlo_price(S, K, r, sigma, T, option_type='call', n_simulations=100_000, seed=42):
    
    #Simulating stock price
    S_T=simulate_terminal_prices(S, K, r, sigma, T, n_simulations, seed)

    #The payoff for each type of option
    if option_type=='call':
        payoff=np.maximum(S_T-K, 0)
    elif option_type=='put':
        payoff=np.maximum(K-S_T, 0)
    else:
        raise ValueError("option type must be 'call' or 'put'")

    #Compute the premium's price (what we would pay today)
    price=np.exp(-r*T) * np.mean(payoff)
    
    # Evaluating the mean spread at 95% confidence
    std_error = np.std(payoff) / np.sqrt(n_simulations)

    lower = np.exp(-r * T) * (np.mean(payoff) - 1.96 * std_error)
    upper = np.exp(-r * T) * (np.mean(payoff) + 1.96 * std_error)

    return price, lower, upper


if __name__== "__main__":
    S=200
    K=150
    r=0.07
    sigma=0.18
    T=1

    mc_call, call_lower, call_upper = monte_carlo_price(S, K, r, sigma, T, option_type='call')
    mc_put, put_lower, put_upper = monte_carlo_price(S, K, r, sigma, T, option_type='put')

    bs_call = call_price(S, K, r, sigma, T)
    bs_put = put_price(S, K, r, sigma, T)

    print("Monte Carlo sim VS Black_Scholes model:")
    print("------------------")
    print(f"MC - Call: {mc_call:.2f} | 95% CI: [{call_lower:.2f}, {call_upper:.2f}] | BS: {bs_call:.2f} | Diff: {abs(mc_call - bs_call):.4f}")
    print(f"MC - Put: {mc_put:.2f} | 95% CI: [{put_lower:.2f}, {put_upper:.2f}] | BS: {bs_put:.2f} | Diff: {abs(mc_put - bs_put):.4f}")