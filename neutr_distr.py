from matplotlib import pyplot as plt
from neutr_approx import spline
from neutr_energ import energ, energ_1
from scipy.integrate import quad
from scipy.special import zetac
from scipy import pi

f = open('neutr_distr_1.dat', 'w')

plt.yscale('log')
plt.xscale('log')

Q = 0.782318 #MeV
eps_0 = 1e-10 #MeV
c = 2.99792458e10 #sm / sec
T_in = 1e10 #K
T_fin = 3e7
tau = 880.1 #sec
T_0 = 2.725 #K
hpl = 1.054e-27 #erg * sec
k = 1.38e-16 #erg / K
const = 2 * (zetac(3) + 1) * 6.1e-10 * 30 * 1.998 * 1e20 * c / tau / Q ** 5 / pi ** 2 / 4

fin_result = []
for i in range(len(energ)):
    eps_0 = energ[i]
    def fn(x):
        return (k * x / hpl / c) ** 3 * spline(x) / x ** 3 * (Q - eps_0 * x / T_0) ** 2
    result = quad(fn, 3e7, 1e10)
    fin_result.append(result[0] * const * eps_0 ** 2)
    f.write(str(eps_0) + ',' + '	' + str(fin_result[i]) + '\n')

fin_result_1 = []
for i in range(len(energ_1)):
    eps_0 = energ_1[i]
    def fn(x):
        return (k * x / hpl / c) ** 3 * spline(x) / x ** 3 * (Q - eps_0 * x / T_0) ** 2
    T_max = Q / energ_1[i] * T_0
    result = quad(fn, 3e7, T_max)
    fin_result_1.append(result[0] * const * eps_0 ** 2)
    f.write(str(eps_0) + ',' + '	' + str(fin_result_1[i]) + '\n')

for i in range(len(energ_1)):
    print(fin_result_1[i])

d_plot = plt.plot(energ_1, fin_result_1, 'bo', label='Original Points')
d_plot = plt.plot(energ, fin_result, 'bo', label='Original Points')
plt.show()

f.close()
