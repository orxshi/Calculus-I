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

print('T1 =', T1)
print('T2 =', T2)
print('Tp1 =', Tp1)
print('Tp2 =', Tp2)
print('T21 =', T21)
print('T22 =', T22)
print('T23 =', T23)


plt.plot(ts, T, 'b')
plt.plot(t1, T1, 'ko')
plt.plot(t2, T2, 'ko')
plt.plot(t2, T21, 'ko')
plt.plot([t1, t2], [tempe(t1), T21], 'r')


# plt.xlabel('r')
# plt.ylabel('A')
# ax.set_yticks([A1, A2, A2a], [r'$4\pi$', r'$25\pi$', r'$16\pi$'])
# ax.annotate('', (r2, A2a), (r2, A2), arrowprops=dict(arrowstyle='<->'))
# ax.text(r2 + 0.2, (A2a + A2) / 2, 'error = ' + r'$9\pi$')

# ax.annotate('', (r1, A1), (r2, A1), arrowprops=dict(arrowstyle='<->'))
# ax.text(r1 + 1.2, A1 - 5.5, r'$\Delta$' + 'r = ' + str(r2 - r1))

# ax.annotate('', (r2, A1), (r2, A2a), arrowprops=dict(arrowstyle='<->'))
# ax.text(r2 + 0.2, (A1 + A2a) / 2, r'$\Delta$' + 'A = 12' + r'$\pi$')







    
    

















# import matplotlib.pyplot as plt
# import numpy as np
# from math import pi
# from ipywidgets import interact
# import ipywidgets as widgets


# with plt.ioff():
#     plt.close()
#     fig, ax = plt.subplots()
#     fig.canvas.header_visible = False

#     r = np.linspace(0, 5)
#     A = pi * r ** 2

#     pp, = plt.plot([], [], 'ko')
#     ppp, = plt.plot([], [], 'r')
#     pppp, = plt.plot([], [], 'ko')
#     Ap = 2 * pi * 2
#     plt.xlim(0, 8)
#     plt.plot(r, A, 'b')
#     plt.plot(2,pi * 2 ** 2,'ko')
#     plt.xlabel('r')
#     plt.ylabel('A')


# ann = []

# aa = widgets.Text(description='Approximated area = ', style={'description_width': 'initial'})
# exact_text = widgets.Text(description='Exact area = ', style={'description_width': 'initial'})
# error_text = widgets.Text(description='Error = ', style={'description_width': 'initial'})
# slider = widgets.BoundedIntText(value=4, min=2, max=5, step=1, description='radius', disabled=False)

# def plot_func(x):
    
#     for _ in ann:
#         _.remove()
#     pp.set_data([x],[pi * x ** 2])
#     ppp.set_data([2, x], [pi * 2 ** 2 + Ap * (2 - 2), pi * 2 ** 2 + Ap * (x - 2)])
#     pppp.set_data([x], [pi * 2 ** 2 + Ap * (x - 2)])
#     app = pi * 2 ** 2 + Ap * (x - 2)
#     exact = pi * x ** 2
#     aa.value = str(round(app))
#     exact_text.value = str(round(exact))
#     error_text.value = str(round(exact - app))
#     ax.set_yticks([4*pi, 16*pi], [r'$4\pi$', r'$16\pi$'])
#     an = ax.annotate('', (x,app), (x,exact), arrowprops=dict(arrowstyle='<->'))
#     ann.append(an)
#     ax.text(x+0.2, (app+exact)/2, 'error')

# interactive_out = widgets.interactive_output(plot_func, {'x': slider})

# vbox = widgets.VBox([slider, aa, exact_text, error_text], layout=widgets.Layout(width='20%'))
# right = widgets.VBox([fig.canvas], layout=widgets.Layout(width='80%'))
# hbox = widgets.HBox([vbox, right])

# display(hbox)