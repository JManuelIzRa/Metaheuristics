import matplotlib.pyplot as plt

### Sustituir los valores ###

mProb =  [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
Accuracy_mProb =  [1.0, 0.9, 1.0, 0.5, 0.6, 0.1, 0.2, 0.1, 0.1, 0.1]
Media_mochila =  [637, 550, 427, 427, 340, 210, 87]
Varianza_mochila =  [0.0, 1589.49, 25568.010000000002, 9017.58024691358, 12588.543209876543, 23340.6875, 46879.666666666664, 1800.75, 4275.36, 32706.5]
Desviacion_mochila =  [0.0, 39.86840854611581, 159.9, 94.96094063831497, 112.1986773980716, 152.77659342975284, 216.51712788291522, 42.4352447854375, 65.38623708396133, 180.84938484827643]

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2)

ax1.plot(mProb,Accuracy_mProb)
ax1.set_title('Accuracy')
ax1.set_xlim(0.1,1)
ax1.set_ylim(0,1.01)

ax2.plot(mProb,Varianza_mochila)
ax2.set_title('Variation')
ax2.set_xlim(0.1,1)

ax3.plot(mProb,Desviacion_mochila)
ax3.set_title('Standard Deviation')
ax3.set_xlim(0.1,1)

ax4.plot(mProb,Media_mochila)
ax4.set_title('Medium value of the population')
ax4.set_xlim(0.1,1)


plt.show()

nSolutions =  [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Accuracy_nSolutions =  [0.8, 0.9, 0.9, 0.825, 0.86, 0.8166666666666667, 0.9285714285714286, 0.925, 0.8444444444444444, 0.93]
Valores_mochila =  [637, 637, 637, 637, 637, 637, 637, 637, 637, 637, 637, 637, 637, 637, 637, 637, 637, 637, 550, 637, 637, 637, 637, 637, 637, 637, 637, 637, 637, 637, 637, 637, 637, 637, 637, 550, 637, 637, 637, 637, 637, 637, 637, 637, 637, 637, 637, 637, 637, 637, 637, 637, 297, 637, 637, 637, 637, 637, 199, 637, 637, 637, 637, 637, 637, 637, 637, 637, 637, 637, 637, 637, 637, 637, 637, 637, 637, 427, 637, 637, 637, 637, 637, 637, 637, 637, 637, 637, 637, 637, 637, 637, 637, 637, 637, 637, 637, 637]
Media_mochila =  [526.5555555555555, 592.5, 607.1724137931035, 619.0277777777778, 627.0454545454545, 617.0566037735849, 619.8088235294117, 626.2307692307693, 623.7349397590361, 625.1428571428571]
Varianza_mochila =  [1238.9135802469134, 18924.75, 12012.832342449467, 5197.527006172841, 4260.997933884298, 5111.864720541116, 6526.272275086504, 2145.562130177515, 2222.917694875889, 3601.061224489795]
Desviacion_mochila =  [35.1982042190637, 137.56725627852, 109.60306721278135, 72.09387634309061, 65.27631985555173, 71.49730568728528, 80.78534690825127, 46.320212976383374, 47.14782810348626, 60.00884288577639]

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2)

ax1.plot(nSolutions,Accuracy_nSolutions)
ax1.set_title('Accuracy')
ax1.set_xlim(10,100)
ax1.set_ylim(0,1.01)

ax2.plot(nSolutions,Varianza_mochila)
ax2.set_title('Variation')
ax2.set_xlim(10,100)

ax3.plot(nSolutions,Desviacion_mochila)
ax3.set_title('Standard Deviation')
ax3.set_xlim(10,100)

ax4.plot(nSolutions,Media_mochila)
ax4.set_title('Medium value of the population')
ax4.set_xlim(10,100)

plt.show()

MaxGenerations =  [100, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 5000, 10000]
Accuracy_maxGenerations =  [0.8, 0.9, 1.0, 0.9, 0.7, 1.0, 0.7, 0.9, 1.0, 1.0, 0.9]
Valores_mochila =  [637, 637, 637, 637, 637, 637, 637, 637, 637]
Media_mochila =  [575.8888888888889, 594.3, 637.0, 603.0, 637.0, 637.0, 594.5, 607.3, 637.0, 637.0, 637.0]
Varianza_mochila =  [29876.54320987654, 16409.61, 0.0, 10404.0, 0.0, 0.0, 12643.75, 7938.8099999999995, 0.0, 0.0, 0.0]
Desviacion_mochila =  [172.84832429004496, 128.1, 0.0, 102.0, 0.0, 0.0, 112.4444307202451, 89.1, 0.0, 0.0, 0.0]

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2)

ax1.plot(MaxGenerations,Accuracy_maxGenerations)
ax1.set_title('Accuracy')
ax1.set_xlim(100,10000)
ax1.set_ylim(0,1.01)

ax2.plot(MaxGenerations,Varianza_mochila)
ax2.set_title('Variation')
ax2.set_xlim(100,10000)

ax3.plot(MaxGenerations,Desviacion_mochila)
ax3.set_title('Standard Deviation')
ax3.set_xlim(100,10000)

ax4.plot(MaxGenerations,Media_mochila)
ax4.set_title('Medium value of the population')
ax4.set_xlim(100,10000)

plt.show()

cProb =  [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
Accuracy_cProb =  [0.5, 0.8, 1.0, 1.0, 0.9, 0.3, 0.7, 0.9, 0.9, 0.9]
Valores_mochila =  [637, 637, 637, 637, 637, 637, 637, 637, 637]
Media_mochila =  [497.22222222222223, 619.6, 637.0, 637.0, 627.2, 446.3333333333333, 528.4, 637.0, 594.3, 637.0]
Varianza_mochila =  [26823.728395061727, 1211.04, 0.0, 0.0, 864.36, 43465.88888888889, 30984.840000000004, 0.0, 16409.61, 0.0]        
Desviacion_mochila =  [163.77951152406618, 34.8, 0.0, 0.0, 29.4, 208.48474497883265, 176.02511184487287, 0.0, 128.1, 0.0]      

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2)

ax1.plot(cProb,Accuracy_cProb)
ax1.set_title('Accuracy')
ax1.set_xlim(0.1,1)
ax1.set_ylim(0,1.01)

ax2.plot(cProb,Varianza_mochila)
ax2.set_title('Variation')
ax2.set_xlim(0.1,1)

ax3.plot(cProb,Desviacion_mochila)
ax3.set_title('Standard Deviation')
ax3.set_xlim(0.1,1)

ax4.plot(cProb,Media_mochila)
ax4.set_title('Medium value of the population')
ax4.set_xlim(0.1,1)


plt.show()

Tournament_size =  [1, 3, 5, 7, 10]
Accuracy_Tournament_size =  [0.1, 1.0, 1.0, 0.9, 1.0]
Valores_mochila =  [620, 620, 620, 620, 620, 620, 620, 620, 620, 620]
Media_mochila =  [254.1, 637.0, 620.0, 628.3, 620.0]
Varianza_mochila =  [3010.8900000000003, 0.0, 0.0, 681.21, 0.0]
Desviacion_mochila =  [54.871577342008315, 0.0, 0.0, 26.1, 0.0]

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2)

ax1.plot(Tournament_size,Accuracy_Tournament_size)
ax1.set_title('Accuracy')
ax1.set_xlim(1,10)
ax1.set_ylim(0,1.01)
ax1.set_ylabel('Accuracy')


ax2.plot(Tournament_size,Varianza_mochila)
ax2.set_title('Variation')
ax2.set_xlim(1,10)


ax3.plot(Tournament_size,Desviacion_mochila)
ax3.set_title('Standard Deviation')
ax3.set_xlim(1,10)


ax4.plot(Tournament_size,Media_mochila)
ax4.set_title('Medium value of the population')
ax4.set_xlim(1,10)


plt.show()