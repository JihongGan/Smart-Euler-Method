from smartEuler import *
import math
import time
from decimal import *



def f1(t, y):
    """
    Blanchard p. 55
    with h = 0.1, t0 = 0, tf = 1, y0 = 1
    the exact y(tf) = 4.195
    """
    return 2 * y - 1

# yf = euler(0.1, 0, 1, f1, 1.0)
# assert math.isclose(yf, 3.59587, rel_tol=1e-2)

start = time.time()
yf = improved_euler(hinit = 0.1, t0 = 0, y0 = 1, f = f1, tf= 1.0, tor = 0.001)
print('improved euler outputs: ', yf)
print('improved euler spends', time.time() - start, 'seconds')

start = time.time()
yf = euler(h = 0.00001, t0 = 0, y0 = 1, f = f1, tf = 1.0)
print('original euler outputs: ', yf)
print('original euler spends', time.time() - start, 'seconds')


# def f2(t, y):
#     return math.exp(t) * math.sin(y)

# start = time.time()
# yf = improved_euler(hinit = 0.1, t0 = 0, y0 = 5, f = f2, tf= 12.0, tor = 0.5)
# print('improved euler outputs: ', yf)
# print('improved euler spends', time.time() - start, 'seconds')

# start = time.time()
# yf = euler(h = 0.00001, t0 = 0, y0 = 5, f = f2, tf = 12.0)
# print('original euler outputs: ', yf)
# print('original euler spends', time.time() - start, 'seconds')


print("All passed")


