import numpy as np

f = open('neutr_energ.txt', 'w')

energ = []
for i in range(-16, -10):
    energy = np.linspace(10 ** i, 10 ** (i + 1) - 10 ** (i - 1), 90)
    for j in range(len(energy)):
        energ.append(energy[j])  

energy = np.linspace(1e-10, 2.1e-10, 12)
for i in range(len(energy)):
    energ.append(energy[i])  

energ_1 = []
energy = np.linspace(2.2e-10, 9.9e-10, 78)
for i in range(len(energy)):
    energ_1.append(energy[i])

for i in range(-9, -8):
    energy = np.linspace(10 ** i, 10 ** (i + 1), 91)
    for j in range(len(energy)):
        energ_1.append(energy[j]) 

energy = np.linspace(1.1e-8, 5e-8, 40)
for i in range(len(energy)):
    energ_1.append(energy[i])

for i in range(len(energ)):
    f.write(str(energ[i]) + '\n')

for i in range(len(energ_1)):
    f.write(str(energ_1[i]) + '\n')

f.close()
