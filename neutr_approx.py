from matplotlib import pyplot as plt
from scipy.interpolate import UnivariateSpline
from numpy import linspace, loadtxt
#from neutron_decay import conc
from Temp_n_time import neu_temp

#f = open('neutr_approx.txt', 'w')

data = loadtxt('nuclei.dat')
x = data[:,0][::-1] # Reversing the input data...
y = data[:,1][::-1]

plt.yscale('log')
plt.xscale('log')

spline = UnivariateSpline(x, y, s=0)

xi = linspace(3e7, x.max(), 25000)
yi = spline(xi) 

appr = spline(x)
differ = abs(appr - y) / y

plt.gca().invert_xaxis()

#p1 = plt.plot(x, differ, 'bo', label='Original Points')
p2 = plt.plot(xi, yi, 'g', label='Interpolated Points')
p3 = plt.plot(x, y, 'bo', label='Original Points')
#p4 = plt.plot(neu_temp, conc, 'bo', label='Original Points')
plt.show()

#f.close()
