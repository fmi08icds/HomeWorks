# plot x^4 + x^3 + x^2 + x + 1

import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize
""" 
# plt.plot(m)
def f1(x):
    return x**4 + x**3 - x**2 - x

def derivativef1(x):
    return 4*x**3 + 3*x**2 - 2*x - 1

def secndderivativef1(x):
    return 12*x**2 + 6*x - 2

x = np.linspace(-2, 2, 100)
argmin = (1+np.sqrt(17))/8
plt.plot(x, f1(x))
plt.plot(x, derivativef1(x), color='red')
plt.plot(x, secndderivativef1(x), color='green')
# write name of the function on the graph
plt.text(-1.5, 10, r'$f(x) = x^4 + x^3 - x^2 - x$')
plt.text(-1.5, 8, r'$f^\prime(x) = 4x^3 + 3x^2 - 2x - 1$')
plt.text(-1.5, 6, r'$f^{\prime\prime}(x) = 12x^2 + 6x - 2$')

plt.title(f'y: {argmin:.2f} at argmin {f1(argmin):.2f}')
plt.axhline(y=0, color='black')

plt.scatter(x=argmin,y= f1(argmin))
plt.show()
 """


f = lambda x, y, eps: 0.3*(x**2 + (eps**2)*(y**2))
fprime = lambda x, y, eps: np.array([0.6*x, 0.6*eps**2*y])
fprime2 = lambda x, y, eps: np.array([[0.6, 0], [0, 0.6*eps**2]])


##  homework 09 ..
optimize.minimize(f, x0=[5],method="Powell", args=(1,0.3), jac=fprime, hess=fprime2)