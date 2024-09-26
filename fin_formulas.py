import numpy as np
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
# print(round(pv, 4))
"""
#  Price (PV) of a coupon bond

def bond_price(pmt, r, m, n, fv):
    cf_pmt = []
    num_coupon_payments = m * n

    for i in range(num_coupon_payments):
        cf_pmt.append(pmt)

    last_cf = cf_pmt.pop(-1)
    cf_pmt.append(last_cf + fv)
    print(cf_pmt)

    cf = cf_pmt

    for x in cf:
        pv = []
        discounted_cf = x * (1 + (r / m)) ** -(m * n)
        pv.append(discounted_cf)

    print(round(sum(pv, 4)))

# bond_price(3, 4, 1, 3, 100)

def bond_price_ii(pmt, r, m, n, fv):
    discounted_cf = []
    cf = [pmt] * (m * n)
    print(cf)

    g = list(range(len(cf) + 1))
    gee = g.pop(0)
    print(g)

    denominator = (1 + (r / m))
    for i in cf:
        discounted_cf = []
        x =  i / (denominator) ** g
        discounted_cf += x
        # x =  i / (1 + (r / m)) ** g[i]
    print(discounted_cf)
    # print(sum(discounted_cf))

bond_price_ii(3,.04, 1, 3, 100) """

# Present value of a coupon bond; pmt and r must be entered as a value per period

def pv_bond(pmt, r, n, m, fv):
    pmt = pmt / m
    r = r / 100 / m
    pv_coupon = pmt * ((1 - (1 / (1 + r) ** (n * m))) / r)
    pv_face = fv / ((1 + r) ** (n * m))

    return pv_coupon + pv_face

# print(pv_bond(3, .04, 3, 100))

# MacaulayDuration

#  m is compounding periods per year
#  r is payment per period
""" cf = [30, 30, 30, 30, 30, 1030]
full_price = 1000
r = .03
frac_coupon = 0
m = 2 """

def mac_dur(cf, full_price, r, m, frac_coupon):
    macaulay_dur = []
    for i in range(len(cf)):
        n = (i+1)
        duration = (n - frac_coupon) * (cf[i]/(1 + r) ** (n - frac_coupon)) / full_price
        macaulay_dur.append(duration)
    if m > 1:
        macaulay_dur_annual = (sum(macaulay_dur) / m)
        print("Annual MacDur is {}".format(round(macaulay_dur_annual, 4)))
    else:
        macaulay_dur_reg = (sum(macaulay_dur))
        print("MacDur is {}".format(round(macaulay_dur_reg , 4)))
    # return round(sum(macaulay_dur),4)

# mac_dur(cf, full_price, r, m, frac_coupon)

# Modified Duration; find pv_minus and pv_plus with the pv_bond formula above
# To find r - add/subtract the change in yield in basis points (ex. original r=4% change in ytm=50bps, enter 4.5 as r in pv_bond)
def mod_duration(pv_0, pv_minus, pv_plus, basis_points):
    bp = basis_points / 100
    mod_dur =  (pv_minus - pv_plus)  / (2 * bp * pv_0)
    return mod_dur

print(mod_duration(100, 101.831, 98.207, .50))

print('\n')