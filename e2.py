import matplotlib.pyplot as plt
import numpy as np
from math import pi


fig, ax = plt.subplots()
# plt.xlim(0, 7)

ts = np.linspace(-7.5, 10)

t1 = -5
t2 = 0

def tempe(t):
    return 1/3 * t ** 3 - 3 * t ** 2 + 8 * t + 10

def tempe_deriv(t):
    return t ** 2 - 6 * t + 8

def tempe_deriv_2(t):
    return 2 * t - 6

def tempe_deriv_3(t):
    return 2

T = [tempe(t) for t in ts]

T1 = tempe(t1)
T2 = tempe(t2)

# first derivative of temperature wrt t at t1
Tp1 = tempe_deriv(t1)
# second derivative of temperature wrt t at t1
Tp2 = tempe_deriv_2(t1)
# third derivative of temperature wrt t at t1
Tp3 = tempe_deriv_3(t1)

# linear approximation of temperature at t2
T21 = T1 + Tp1 * (t2 - t1)

# quadratic approximation of temperature at t2
T22 = T21 + 0.5 * Tp2 * (t2 - t1) ** 2

# cubic approximation of temperature at t2
T23 = T22 + Tp3 / 6 * (t2 - t1) ** 3

# print('T1 =', T1)
# print('T2 =', T2)
# print('Tp1 =', Tp1)
# print('Tp2 =', Tp2)
# print('T21 =', T21)
# print('T22 =', T22)
# print('T23 =', T23)

plt.plot(ts, T, 'b')
plt.plot(t1, T1, 'ko')
plt.plot(t2, T2, 'ko')
plt.plot(t2, T21, 'ko')
plt.plot([t1, t2], [tempe(t1), T21], 'r')