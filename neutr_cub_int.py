import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline
from scipy.integrate import quad

data = np.loadtxt('nuclei.dat')
x = data[:,0][::-1] # Reversing the input data...
y = data[:,1][::-1]

plt.yscale('log')
plt.xscale('log')

spl = InterpolatedUnivariateSpline(x, y)

#result = quad(lambda x: spl(x), 1, 2)

#print(result[0])

plt.gca().invert_xaxis()

plt.plot(x, y, 'ro', ms=5)
xs = np.linspace(3e7, x.max(), 10000)
plt.plot(xs, spl(xs), 'g', lw=3, alpha=0.7)
plt.show()


