from matplotlib import pyplot as plt
from Temp_n_time import neu_temp, neu_time
from scipy.interpolate import UnivariateSpline
from neutr_energ import energ, energ_1
from numpy import linspace, loadtxt
#from neutr_distr import fin_result, fin_result_1
from scipy import pi
from math import log, exp

#f = open('neutron_decay_1.dat', 'w')

data = loadtxt('TEMP_and_TIME.dat')
x = data[:,0]
y = data[:,1]

data = loadtxt('nuclei.dat')
te = data[:,0]
ne = data[:,1]

tts = UnivariateSpline(x, y, s = 0)

tau = 880.1 #sec
n_0 = 1.18454073443893E-008 #cm ** (-3)
t_0 = 5490.365856932339 #sec

conc = []
temp = []
time = []
for i in range(186,278):
    result = n_0 * exp((t_0 - tts(x[i])) / tau)
    conc.append(result)
    temp.append(x[i])
    time.append(tts(x[i]))

#for i in range(len(conc)):
#    print(temp[i],time[i],conc[i])

plt.gca().invert_xaxis()

plt.yscale('log')
plt.xscale('log')

d_plot = plt.plot(te, ne, 'bo', label='Original Points')
d_plot = plt.plot(temp, conc, 'ro', label='Original Points')
plt.show()

tau = 880.1 #sec
n_0 = 0.0001545254 #cm ** (-3)
t_0 = 342.0002319860956 #sec

conc = []
temp = []
time = []
for i in range(250,332):
    result = n_0 * exp((t_0 - tts(x[i])) / tau)
    conc.append(result)
    temp.append(x[i])
    time.append(tts(x[i]))

#for i in range(len(conc)):
#    print(temp[i],time[i],conc[i])

plt.gca().invert_xaxis()

plt.yscale('log')
plt.xscale('log')

d_plot = plt.plot(te, ne, 'bo', label='Original Points')
d_plot = plt.plot(temp, conc, 'ro', label='Original Points')
plt.show()

tau = 880.1 #sec
n_0 = 5.65874338736091E-007 #cm ** (-3)
t_0 = 613.0889022713407 #sec

conc = []
temp = []
time = []
for i in range(260,314):
    result = n_0 * exp((t_0 - tts(x[i])) / tau)
    conc.append(result)
    temp.append(x[i])
    time.append(tts(x[i]))

#for i in range(len(conc)):
#    print(temp[i],time[i],conc[i])

plt.gca().invert_xaxis()

plt.yscale('log')
plt.xscale('log')

d_plot = plt.plot(te, ne, 'bo', label='Original Points')
d_plot = plt.plot(temp, conc, 'ro', label='Original Points')
plt.show()

tau = 880.1 #sec
n_0 = 8.39266715966233E-008 #cm ** (-3)
t_0 = 1376.1312049757578 #sec

conc = []
temp = []
time = []
for i in range(240,296):
    result = n_0 * exp((t_0 - tts(x[i])) / tau)
    conc.append(result)
    temp.append(x[i])
    time.append(tts(x[i]))

#for i in range(len(conc)):
#    print(temp[i],time[i],conc[i])

plt.gca().invert_xaxis()

plt.yscale('log')
plt.xscale('log')

d_plot = plt.plot(te, ne, 'bo', label='Original Points')
d_plot = plt.plot(temp, conc, 'ro', label='Original Points')
plt.show()

#f.close()
