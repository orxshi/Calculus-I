import matplotlib.pyplot as plt
import numpy as np
from math import pi


fig, ax = plt.subplots()
plt.xlim(0, 7)

R = np.linspace(0, 5)

r1 = 2
r2 = 5

def area(r):
    return pi * r ** 2

A = [area(r) for r in R]

A1 = area(r1)
A2 = area(r2)

# derivative of area wrt r at r1
Ap = 2 * pi * r1

# approximated area at r2
A2a = A1 + Ap * (r2 - r1)


plt.plot(R, A, 'b')
plt.plot(r1, A1, 'ko')
plt.plot(r2, A2, 'ko')
plt.plot(r2, A2a, 'ko')
plt.plot([r1, r2], [area(r1), A2a], 'r')


# plt.xlabel('r')
# plt.ylabel('A')
ax.set_yticks([A1, A2, A2a], [r'$4\pi$', r'$25\pi$', r'$16\pi$'])
ax.annotate('', (r2, A2a), (r2, A2), arrowprops=dict(arrowstyle='<->'))
ax.text(r2 + 0.2, (A2a + A2) / 2, 'error = ' + r'$9\pi$')

ax.annotate('', (r1, A1), (r2, A1), arrowprops=dict(arrowstyle='<->'))
ax.text(r1 + 1.2, A1 - 5.5, r'$\Delta$' + 'r = ' + str(r2 - r1))

ax.annotate('', (r2, A1), (r2, A2a), arrowprops=dict(arrowstyle='<->'))
ax.text(r2 + 0.2, (A1 + A2a) / 2, r'$\Delta$' + 'A = 12' + r'$\pi$')