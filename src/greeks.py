from scipy.stats import norm
import numpy as np
from black_scholes import calculate_d1, calculate_d2

#Calculate Greeks: Delta
def delta(S, K, T, r, sigma, option_type = 'call'):
    d1 = calculate_d1(S, K, T, r, sigma)

    if option_type == 'call':
        return norm.cdf(d1)
    elif option_type == 'put':
        return norm.cdf(d1) - 1
    else:
        raise ValueError("Option type must be 'call' or 'put'")

#Gamma
def gamma(S, K, T, r, sigma):
    d1=calculate_d1(S, K, T, r, sigma)
    return norm.pdf(d1) / (S * sigma * np.sqrt(T))

#Vega
def vega(S, K, T, r ,sigma):
    d1 = calculate_d1(S, K, T, r, sigma)
    return S * norm.pdf(d1) * np.sqrt(T) / 100

#Theta
def theta(S, K, T, r, sigma, option_type = "call"):
    d1 = calculate_d1(S, K, T, r, sigma)
    d2 = calculate_d2(S, K, T, r, sigma)
    first_term = -(S * norm.pdf(d1) * sigma) / (2 * np.sqrt(T))

    if option_type == "call":
        second_term = r * K * np.exp(-r * T) * norm.cdf(d2)
        return (first_term - second_term) / 365
    elif option_type == "put":
        second_term = r * K * np.exp(-r * T) * norm.cdf(-d2)
        return (first_term + second_term) / 365
    else:
        raise ValueError("Option_type must be call put or call")
    
#Rho
def rho(S, K, T, r, sigma, option_type="call"):
    d2 = calculate_d2(S, K, T, r, sigma)

    if option_type == "call":
        return K * T * np.exp(-r * T) * norm.cdf(d2) / 100
    elif option_type == "put":
        return -K * T * np.exp(-r * T) * norm.cdf(-d2) / 100
    else:
        raise ValueError ("Option_type must be 'call or 'put'")

if __name__ == "__main__":
    S = 150
    K = 130
    T = 1
    r = 0.04
    sigma = 0.03

    print("Call Delta:", delta(S, K, T, r, sigma, "call"))
    print("Put Delta:", delta(S, K, T, r, sigma, "put"))
    print("Gamma:", gamma(S, K, T, r, sigma))
    print("Vega:", vega(S, K, T, r, sigma))
    print("Call Theta:", theta(S, K, T, r, sigma, "call"))
    print("Put Theta:", theta(S, K, T, r, sigma, "put"))
    print("Call Rho:", rho(S, K, T, r, sigma, "call"))
    print("Put Rho:", rho(S, K, T, r, sigma, "put"))