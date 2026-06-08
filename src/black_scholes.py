# Black and Scholes option pricing model

#installing necessary libraries
import numpy as np
from scipy.stats import norm

#Make sure the inputs are valid
def validate_inputs(S, K, r, sigma, T):

    '''Where: 
    S: Current asset price
    K: Strike price
    T: Time to maturity
    r: Risk-free rate
    sigma: Volatility
    '''
    # Setting the conditions that can't be broken
    if S <= 0:
        raise ValueError ("Stock price must be positive")
    if K <= 0:
        raise ValueError("Strike needs to be positive")
    if T<= 0:
        raise ValueError("Time can't be negative")
    if sigma <= 0:
        raise ValueError("volatilty cannot by nul or negative")
    return True

#Calculating d1 (the hedge ratio required)
def calculate_d1(S, K, r, sigma, T):
    validate_inputs(S, K, r, sigma, T)
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    
    return d1

#Calculating d2 (To see if we will be able to exercise the option, to see if we are in the money)
def calculate_d2(S, K, r, sigma, T):
    validate_inputs(S, K, r, sigma, T)
    d1 = calculate_d1(S, K, r, sigma, T)  
    d2 = d1 - sigma * np.sqrt(T)
    
    return d2

''' Computing the call price: Call = S * N(d1) - K * exp(-rT) * N(d2)'''
def call_price(S, K, r, sigma, T):

    #Instructing how the equation should define d1 and d2 to compute the cumulative distributions
    d1 = calculate_d1(S, K, r, sigma, T)
    d2 = calculate_d2(S, K, r, sigma, T)

    #Inputs are defined, calculating the call price:
    call = S * norm.cdf(d1) - K * np.exp(-r*T) * norm.cdf(d2)
    
    return call

'''Computing the put price: p = K * exp(-rT) * N(d2) - S * N(d1)'''
def put_price(S, K, r, sigma, T):
    
    #Same as for the call price, we need to instruct the equation to compute d1 and d2 beforehand
    d1 = calculate_d1(S, K, r, sigma, T)
    d2 = calculate_d2(S, K, r, sigma, T)

    #Calculating the put price:
    put = K * np.exp(-r*T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    
    return put

# Creating a testing block to execute directly when called, to test the model
if __name__ == "__main__":
    S = 200
    K = 150
    r = 0.07
    sigma = 0.18
    T = 1

    call = call_price(S, K, r, sigma, T)
    put = put_price(S, K, r, sigma, T)

    print("BS European option price:")
    print("-------------------------")
    print(f"Call Price: {call:.2f}")
    print(f"Put Price: {put:.2f}")

