import math

print('\n')

# Geometric Mean Return

returns = [.1, .1, .5, .6]
def geometric_return(returns):
    current_return = []
    for i in returns:
        total_return =  (1 + i)
        current_return.append(total_return)

    return round(math.prod(current_return) ** (1 / len(returns)) - 1, 4)

# print(geometric_return(returns))

# Future Value calculation for 'n' number of years with 1 compounding period per year

def future_value(n, i, pv):
    return pv * (1 + i) ** n

# print(round(future_value(2,.10,100), 4))

# Present Value calculation for 'n' number of years wth 'm' compounding periods per year

def present_value(n, m, i, fv):
    return fv * (1 + (i/m)) ** -(m * n)

# print(round(present_value(2,1,.10,121), 4))

# NPV
# ex. first number is cf_0

cf = [50, 60,70]
r = .04

pv = 0
for i in range(len(cf)):
    pv += cf[i] / (1 + r) ** (i)
print(round(pv, 4))

# MacaulayDuration

""" cf = [3.7, 4.9, 107]
full_price = 95
r = .06
frac_coupon = 0 """

def mac_dur(cf, full_price, r, frac_coupon):
    macaulay_dur = []
    for i in range(len(cf)):
        n = (i+1)
        duration = (n - frac_coupon)*(cf[i]/(1+r)**(n - frac_coupon))/full_price
        macaulay_dur.append(duration)
    return round(sum(macaulay_dur),3)


# print(mac_dur(cf, full, r, frac_coupon))

print('\n')