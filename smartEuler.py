import math
from decimal import *
import time


# set precision of decimals to 10 digits
getcontext().prec = 15



def one_step(h, tn, yn, f):
    """
    Conducts one step of Euler's method.
    Returns a decimal or float to be the estimation of the current step.

    h: decimal or float, the step size
    yn: decimal or float, the estimation from the previous step
    tn: decimal or float, the time variable from the previous step
    f: callable function f(t, y), our target single variable ODE"""

    return yn + h * Decimal(f(tn, yn))

def euler(h, t0, y0, f, tf):
    """
    Euler's method with fixed step size.
    Returns a decimal to be the approximation of the value of the IVP at tf.

    h: float, the fixed step size
    t0: float, the time index of the IVP
    y0: float, the initial value of the IVP
    f: callable function f(t, y), our target single variable ODE
    tf: float, the end time endex when the approximation is returned"""

    tn = Decimal(str(t0))
    tf = Decimal(str(tf))
    h = Decimal(str(h)) #convert to decimals instead of floats to avoid error
    yn = y0
    iter = 0
    while tn < tf:
        yn = one_step(h, tn, yn, f)
        tn = tn + h
        iter = iter + 1
    if tn != tf:
        yn = one_step(tf - tn + h, tn - h, yn, f)
    print('# of iterations for euler is: ', iter)
    return yn

def improved_euler(hinit, t0, y0, f, tf, tor):
    """
    Euler's method with adaptive step size.
    Returns a decimal to be the approximation of the value of the IVP at tf.

    hinit: float, the initial step size
    t0: float, the time index of the IVP
    y0: float, the initial value of the IVP
    f: callable function f(t, y), our target single variable ODE
    tf: float, the end time endex where we retrun the approximation
    tor: float, tolerance of LTE"""

    hn = Decimal(str(hinit))
    tn = Decimal(str(t0))
    tf = Decimal(str(tf))
    tor = Decimal(str(tor))
    yn = y0
    iter = 0
    while tn < tf:
        a1 = one_step(hn, tn, yn, f)
        a2 = one_step(hn/2, tn+hn/2, one_step(hn/2, tn, yn, f), f)
        lte = (a1 - a2) / hn
        if abs(lte) > tor:
            hn = Decimal('0.9') * tor / abs(lte) * hn
        else:
            yn = 2 * a2 - a1
            tn = tn + hn
            hn = min(Decimal('0.9') * tor / abs(lte) * hn, tf - tn)
        iter = iter + 1
    print('# of iterations for improved euler is: ', iter)
    return yn
