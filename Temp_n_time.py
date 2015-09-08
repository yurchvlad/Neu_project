from numpy import linspace
from scipy.integrate import quad
import math
from math import sqrt

f = open('neutron_temperature.dat', 'w')

const_1 = 1e19 / 7.204
const_2 = 1.78e8
const_3 = 1.78e20

neu_temp = []
neu_time = []

temp = []
temp = linspace(8.61e6, 1e7, 140)
temp_1 = linspace(1e7, 3e7, 3)
for j in range(len(temp_1)):
    neu_temp.append(temp_1[j])
    neu_time.append(const_3 / temp[j] ** 2)

neu_temp.sort(reverse = True)
neu_time.sort()
    
for i in range(len(neu_temp)):
    f.write('%e	%e \n' % (neu_temp[i], neu_time[i]))

f.close()
