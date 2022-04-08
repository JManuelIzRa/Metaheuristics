import matplotlib.pyplot as plt

plt.rcParams.update({'figure.figsize':(7.5,5), 'figure.dpi':100})

mProb =  [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
Accuracy_mProb =  [0.8199999999999997, 0.7254999999999998, 0.6429999999999992, 0.5452499999999989, 0.470199999999998, 0.4139999999999974, 0.37257142857142694, 0.3400000000000012, 0.3143333333333368, 0.2942000000000052]
Media_mochila_mProb =  [12758880.548654761, 12653522.486833328, 12473970.106510572, 12292693.87325297, 12055617.00336269, 11897446.496855807, 11751227.834687063, 11601023.209644333, 11462914.19757097, 11376641.383363873]
Varianza_mochila_mProb =  [532209828596.589, 673327733600.2788, 921993147200.1581, 1110002830907.9937, 1297990931697.4866, 1432688467320.292, 1521299784533.5977, 1675458561224.9268, 1811545796749.463, 1869814419501.6702]
Desviacion_mochila_mProb =  [430682.14847729175, 548144.176523479, 696975.913641728, 808579.4244144051, 903744.9778114946, 973911.149137069, 1024632.9952819163, 1082178.5553228597, 1138648.0610036657, 1165227.2002456135]

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2)

ax1.plot(mProb,Accuracy_mProb)
ax1.set_title('Accuracy')
ax1.set_xlim(0.1,1)
ax1.set_ylim(0,1.01)
ax1.get_yaxis().get_major_formatter().set_useOffset(False)

ax2.plot(mProb,Varianza_mochila_mProb)
ax2.set_title('Variance')
ax2.set_xlim(0.1,1)
ax2.get_yaxis().get_major_formatter().set_useOffset(False)

ax3.plot(mProb,Desviacion_mochila_mProb)
ax3.set_title('Standard Deviation')
ax3.set_xlim(0.1,1)
ax3.get_yaxis().get_major_formatter().set_useOffset(False)

ax4.plot(mProb,Media_mochila_mProb)
ax4.set_title('Medium value of the population')
ax4.set_xlim(0.1,1)
ax4.get_yaxis().get_major_formatter().set_useOffset(False)

plt.tight_layout()
plt.savefig('05.MutationProb_behaviour.png')

nSolutions =  [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Accuracy_nSolutions =  [0.839, 0.7974999999999999, 0.7430000000000004, 0.6961250000000005, 0.64098, 0.5919833333333331, 0.548740816326531, 0.5122107142857143, 0.47508853615520347, 0.4432196825396826]
Media_mochila_nSolutions =  [12697105.18109524, 12773083.360144276, 12804240.926624525, 12806436.39833984, 12804914.37828386, 12791568.212179, 12775427.932097996, 12763643.929556912, 12748271.675336923, 12728469.217922552]
Varianza_mochila_nSolutions =  [549915650580.547, 449971996626.23267, 450202573434.5442, 495668902960.59283, 528168896784.25964, 558365126826.2023, 594284028229.231, 628286976745.1627, 653880228852.9546, 690981932370.4352]
Desviacion_mochila_nSolutions = [425573.018040924, 415362.18614378385, 458329.67944526, 507820.84009189054, 550722.1148340309, 588547.0302674539, 624423.5214300721, 656748.1657836189, 683018.1756715197, 712367.790357586]

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2)

ax1.plot(nSolutions,Accuracy_nSolutions)
ax1.set_title('Accuracy')
ax1.set_xlim(10,100)
ax1.set_ylim(0,1.01)
ax1.get_yaxis().get_major_formatter().set_useOffset(False)

ax2.plot(nSolutions,Varianza_mochila_nSolutions)
ax2.set_title('Variance')
ax2.set_xlim(10,100)
ax2.get_yaxis().get_major_formatter().set_useOffset(False)

ax3.plot(nSolutions,Desviacion_mochila_nSolutions)
ax3.set_title('Standard Deviation')
ax3.set_xlim(10,100)
ax3.get_yaxis().get_major_formatter().set_useOffset(False)

ax4.plot(nSolutions,Media_mochila_nSolutions)
ax4.set_title('Medium value of the population')
ax4.set_xlim(10,100)
ax4.get_yaxis().get_major_formatter().set_useOffset(False)

plt.tight_layout()
plt.savefig('01.NSolutions_behaviour.png')

MaxGenerations =  [100, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 5000, 10000]
Accuracy_maxGenerations =  [0.8549999999999995, 0.8620000000000008, 0.8716666666666678, 0.8747499999999995, 0.8787999999999982, 0.8801666666666641, 0.8812857142857107, 0.8807499999999959, 0.8797777777777728, 0.8799999999999946, 0.8801818181818122]
Media_mochila_maxGenerations =  [12914095.624821423, 13002579.010101188, 13046884.094539681, 13079616.552229164, 13103654.69761666, 13116773.189254625, 13136193.334880946, 13144554.547845228, 13152863.236843906, 13166886.786084915, 13179570.99734234]
Varianza_mochila_maxGenerations =  [466365467564.09735, 450016107384.6234, 493037481037.1947, 495409092269.37244, 496076228937.17737, 516121431746.9316, 485213349932.7835, 481329027249.8541, 486359487852.49304, 470999032574.9031, 460538219870.69794]
Desviacion_mochila_maxGenerations =  [375721.2066377673, 370809.57485995727, 396815.51589523425, 387921.7181775069, 383829.754295087, 393172.9496482812, 377033.82852205244, 379823.0404091235, 380099.73278508405, 369384.3653440088, 364322.8840813556]

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2)

ax1.plot(MaxGenerations,Accuracy_maxGenerations)
ax1.set_title('Accuracy')
ax1.set_xlim(100,10000)
ax1.set_ylim(0,1.01)
ax1.get_yaxis().get_major_formatter().set_useOffset(False)

ax2.plot(MaxGenerations,Varianza_mochila_maxGenerations)
ax2.set_title('Variance')
ax2.set_xlim(100,10000)
ax2.get_yaxis().get_major_formatter().set_useOffset(False)

ax3.plot(MaxGenerations,Desviacion_mochila_maxGenerations)
ax3.set_title('Standard Deviation')
ax3.set_xlim(100,10000)
ax3.get_yaxis().get_major_formatter().set_useOffset(False)

ax4.plot(MaxGenerations,Media_mochila_maxGenerations)
ax4.set_title('Medium value of the population')
ax4.set_xlim(100,10000)
ax4.get_yaxis().get_major_formatter().set_useOffset(False)

plt.tight_layout()
plt.savefig('02.MaxGenerations_behaviour.png')

cProb =  [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
Accuracy_cProb =  [0.6530000000000001, 0.6445000000000002, 0.6486666666666668, 0.6735000000000002, 0.7007999999999994, 0.7216666666666655, 0.7375714285714268, 0.7541249999999969, 0.768222222222218, 0.7737999999999954]
Media_mochila_cProb =  [12762854, 12762854, 12762854, 12762854, 12762854, 12762854, 12762854, 12762854, 12762854, 12762854]
#Varianza_mochila =  [26823.728395061727, 1211.04, 0.0, 0.0, 864.36, 43465.88888888889, 30984.840000000004, 0.0, 16409.61, 0.0]        
#Desviacion_mochila =  [163.77951152406618, 34.8, 0.0, 0.0, 29.4, 208.48474497883265, 176.02511184487287, 0.0, 128.1, 0.0]      

fig, ax = plt.subplots()

ax.plot(cProb,Accuracy_cProb)
ax.set_title('Accuracy')
ax.set_xlim(0.1,1)
ax.set_ylim(0,1.01)
ax.get_yaxis().get_major_formatter().set_useOffset(False)

plt.tight_layout()
plt.savefig('04.CrossoverProb_behaviour.png')

Tournament_size =  [1, 3, 5, 7, 10]
Accuracy_Tournament_size =  [0.15299999999999978, 0.4904999999999998, 0.6080000000000003, 0.6800000000000006, 0.7175999999999993]
Media_mochila =  [12887729, 12887729, 12887729, 12887729, 12887729]

fig, ax = plt.subplots()

ax.plot(Tournament_size,Accuracy_Tournament_size)
ax.set_title('Accuracy')
ax.set_xlim(1,10)
ax.set_ylim(0,1.01)
ax.set_ylabel('Accuracy')
ax.get_yaxis().get_major_formatter().set_useOffset(False)

plt.tight_layout()
plt.savefig('03.TournamentSize_behaviour.png')


######################
###ELITISM############
######################


mProb =  [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
Accuracy_mProb_elitism =  [0.8510000000000001, 0.7790000000000002, 0.6833333333333332, 0.5944999999999995, 0.5169999999999992, 0.45400000000000224, 0.4048571428571478, 0.36700000000000704, 0.33755555555556427, 0.31400000000001005]
Media_mochila_elitism =  [12829767.909174599, 12730450.430746034, 12558371.066133602, 12400815.628762899, 12267683.668796038, 12114184.071963636, 11985301.799603192, 11891257.239722727, 11777448.550314825, 11695474.040640492]
Varianza_mochila_elitism =  [279029835036.7612, 516718616881.8098, 799688462407.0823, 1058279307528.0038, 1252854781409.1133, 1441578442820.9468, 1607176111330.7285, 1699586456221.7402, 1853695963198.6423, 1986451689642.3694]
Desviacion_mochila_elitism =  [261997.00576621067, 438908.0534434483, 615554.4042852063, 762444.9737518745, 859812.3808296772, 952917.9366599501, 1032889.7419646612, 1084726.2538226563, 1147529.8375182587, 1195926.1332923558]

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2)

ax1.plot(mProb,Accuracy_mProb,color='blue',label="Without Elitism")
ax1.set_title('Accuracy')
ax1.set_xlim(0.1,1)
ax1.set_ylim(0,1.01)
ax1.get_yaxis().get_major_formatter().set_useOffset(False)

ax2.plot(mProb,Varianza_mochila_mProb,color='blue',label="Without Elitism")
ax2.set_title('Variance')
ax2.set_xlim(0.1,1)
ax2.get_yaxis().get_major_formatter().set_useOffset(False)

ax3.plot(mProb,Desviacion_mochila_mProb,color='blue',label="Without Elitism")
ax3.set_title('Standard Deviation')
ax3.set_xlim(0.1,1)
ax3.get_yaxis().get_major_formatter().set_useOffset(False)

ax4.plot(mProb,Media_mochila_mProb,color='blue',label="Without Elitism")
ax4.set_title('Medium value of the population')
ax4.set_xlim(0.1,1)
ax4 .get_yaxis().get_major_formatter().set_useOffset(False)

ax1.plot(mProb,Accuracy_mProb_elitism,color='orange',label="With Elitism")
ax1.set_title('Accuracy')
ax1.set_xlim(0.1,1)
ax1.set_ylim(0,1.01)
ax1.get_yaxis().get_major_formatter().set_useOffset(False)

ax2.plot(mProb,Varianza_mochila_elitism,color='orange',label="With Elitism")
ax2.set_title('Variance')
ax2.set_xlim(0.1,1)
ax2.get_yaxis().get_major_formatter().set_useOffset(False)

ax3.plot(mProb,Desviacion_mochila_elitism,color='orange',label="With Elitism")
ax3.set_title('Standard Deviation')
ax3.set_xlim(0.1,1)
ax3.get_yaxis().get_major_formatter().set_useOffset(False)

ax4.plot(mProb,Media_mochila_elitism,color='orange',label="With Elitism")
ax4.set_title('Medium value of the population')
ax4.set_xlim(0.1,1)
ax4 .get_yaxis().get_major_formatter().set_useOffset(False)

plt.legend()
plt.tight_layout()
plt.savefig('05.MutationProb_withElitism_behaviour.png')

nSolutions =  [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Accuracy_nSolutions_elitism =  [0.871, 0.8032499999999999, 0.7600555555555563, 0.7234166666666669, 0.691893333333333, 0.6529111111111102, 0.6092911564625847, 0.5709266369047614, 0.5414162698412701, 0.5099846428571426]
Media_mochila_elitism =  [12869428.0660754, 12883639.57303757, 12880157.064425468, 12893459.076801129, 12898273.945141127, 12901524.949750744, 12895669.764525883, 12879262.186147453, 12865400.052138263, 12850141.66628224]
Varianza_mochila_elitism =  [239400005694.7, 335273954458.48303, 451244429218.76556, 472349029850.3633, 499983415147.36115, 526239121721.14874, 552636843130.7808, 596147083236.9547, 638626689690.012, 669393400634.1884]
Desviacion_mochila_elitism = [197709.09489080834, 307677.7130839094, 425275.05554288375, 470832.12588512356, 517448.409948345, 552058.9598827102, 584343.600083545, 622965.0089249773, 658165.4515536464, 683380.980090186]

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2)

ax1.plot(nSolutions,Accuracy_nSolutions,color='blue',label="Without Elitism")
ax1.set_title('Accuracy')
ax1.set_xlim(10,100)
ax1.set_ylim(0,1.01)
ax1.get_yaxis().get_major_formatter().set_useOffset(False)

ax2.plot(nSolutions,Varianza_mochila_nSolutions,color='blue',label="Without Elitism")
ax2.set_title('Variance')
ax2.set_xlim(10,100)
ax2.get_yaxis().get_major_formatter().set_useOffset(False)

ax3.plot(nSolutions,Desviacion_mochila_nSolutions,color='blue',label="Without Elitism")
ax3.set_title('Standard Deviation')
ax3.set_xlim(10,100)
ax3.get_yaxis().get_major_formatter().set_useOffset(False)

ax4.plot(nSolutions,Media_mochila_nSolutions,color='blue',label="Without Elitism")
ax4.set_title('Medium value of the population')
ax4.set_xlim(10,100)
ax4 .get_yaxis().get_major_formatter().set_useOffset(False)

ax1.plot(nSolutions,Accuracy_nSolutions_elitism,color='orange',label="With Elitism")
ax1.set_title('Accuracy')
ax1.set_xlim(10,100)
ax1.set_ylim(0,1.01)
ax1.get_yaxis().get_major_formatter().set_useOffset(False)

ax2.plot(nSolutions,Varianza_mochila_elitism,color='orange',label="With Elitism")
ax2.set_title('Variance')
ax2.set_xlim(10,100)
ax2.get_yaxis().get_major_formatter().set_useOffset(False)

ax3.plot(nSolutions,Desviacion_mochila_elitism,color='orange',label="With Elitism")
ax3.set_title('Standard Deviation')
ax3.set_xlim(10,100)
ax3.get_yaxis().get_major_formatter().set_useOffset(False)

ax4.plot(nSolutions,Media_mochila_elitism,color='orange',label="With Elitism")
ax4.set_title('Medium value of the population')
ax4.set_xlim(10,100)
ax4 .get_yaxis().get_major_formatter().set_useOffset(False)

plt.legend()
plt.tight_layout()
plt.savefig('01.NSolutions_withElitism_behaviour.png')

MaxGenerations_elitism =  [100, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 5000, 10000]
Accuracy_maxGenerations_elitism =  [0.855, 0.8675000000000003, 0.8610000000000004, 0.8662499999999995, 0.8745999999999992, 0.8748333333333314, 0.8688571428571404, 0.8723749999999972, 0.8716666666666641, 0.8729999999999971, 0.8674545454545426]
Media_mochila_elitism =  [12897423.459353175, 13008716.09800992, 13059214.447395502, 13099716.411322415, 13132992.87563571, 13145220.17081349, 13158913.216060663, 13170718.013931544, 13179920.959926363, 13188489.403706348, 13188509.008488096]
Varianza_mochila_elitism =  [345766992187.50836, 293223137195.9967, 261550201846.40616, 264645259633.37668, 240223117852.5757, 259997960150.25687, 256521679844.95932, 263660253057.02997, 261684670348.88412, 262697955589.10632, 280783065962.42145]
Desviacion_mochila_elitism =  [253681.61177215708, 235046.2107993938, 227457.71756610568, 226201.87798572966, 212546.43516303084, 230221.7348404713, 228529.9424954694, 230255.7414034404, 225955.51883575539, 224122.81752134353, 233700.38712752433]

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2)

ax1.plot(MaxGenerations,Accuracy_maxGenerations, color='blue',label="Without Elitism")
ax1.set_title('Accuracy')
ax1.set_xlim(100,10000)
ax1.set_ylim(0,1.01)
ax1.get_yaxis().get_major_formatter().set_useOffset(False)

ax2.plot(MaxGenerations,Varianza_mochila_maxGenerations,color='blue',label="Without Elitism")
ax2.set_title('Variance')
ax2.set_xlim(100,10000)
ax2.get_yaxis().get_major_formatter().set_useOffset(False)

ax3.plot(MaxGenerations,Desviacion_mochila_maxGenerations,color='blue',label="Without Elitism")
ax3.set_title('Standard Deviation')
ax3.set_xlim(100,10000)
ax3.get_yaxis().get_major_formatter().set_useOffset(False)

ax4.plot(MaxGenerations,Media_mochila_maxGenerations,color='blue',label="Without Elitism")
ax4.set_title('Medium value of the population')
ax4.set_xlim(10,100)
ax4 .get_yaxis().get_major_formatter().set_useOffset(False)

ax1.plot(MaxGenerations,Accuracy_maxGenerations_elitism,color='orange',label="With Elitism")
ax1.set_title('Accuracy')
ax1.set_xlim(100,10000)
ax1.set_ylim(0,1.01)
ax1.get_yaxis().get_major_formatter().set_useOffset(False)

ax2.plot(MaxGenerations,Varianza_mochila_elitism,color='orange',label="With Elitism")
ax2.set_title('Variance')
ax2.set_xlim(100,10000)
ax2.get_yaxis().get_major_formatter().set_useOffset(False)

ax3.plot(MaxGenerations,Desviacion_mochila_elitism,color='orange',label="With Elitism")
ax3.set_title('Standard Deviation')
ax3.set_xlim(100,10000)
ax3.get_yaxis().get_major_formatter().set_useOffset(False)

ax4.plot(MaxGenerations,Media_mochila_elitism,color='orange',label="With Elitism")
ax4.set_title('Medium value of the population')
ax4.set_xlim(100,10000)
ax4 .get_yaxis().get_major_formatter().set_useOffset(False)

plt.legend()
plt.tight_layout()
plt.savefig('02.MaxGenerations_withElitism_behaviour.png')

cProb_eiltism =  [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
Accuracy_cProb_elitism =  [0.18499999999999983, 0.26750000000000024, 0.3716666666666663, 0.45024999999999954, 0.5005999999999998, 0.5401666666666665, 0.584, 0.6168749999999998, 0.6466666666666662, 0.6731999999999991]
Media_mochila_elitism =  [11643432.706805553, 11843504.554365074, 12028775.345701056, 12193832.873102183, 12283913.85535635, 12359813.962487433, 12429956.734607713, 12485529.733054573, 12528462.50220548, 12566836.685687708]
Varianza_mochila_elitism =  [910861346529.798, 928516422972.734, 859189244441.0999, 754097876953.2935, 734796159713.6248, 695670206600.0815, 641116532030.924, 589157294657.8583, 540335354758.0942, 506731406597.289]
Desviacion_mochila_elitism =  [666648.0145082935, 669236.3759606953, 618915.592536679, 554031.8150030642, 534755.6006553086, 506743.0109045006, 466994.64411077404, 436132.3456947148, 408293.59297071595, 384500.28080908203]

fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2)

ax1.plot(cProb,Accuracy_cProb,color='blue',label="Without Elitism")
ax1.set_title('Accuracy')
ax1.set_xlim(0.1,1)
ax1.set_ylim(0,1.01)
ax1.get_yaxis().get_major_formatter().set_useOffset(False)

#ax2.plot(cProb,Varianza_mochila_cProb,color='blue',label="Without Elitism")
#ax2.set_title('Variance')
#ax2.set_xlim(0.1,1)
#ax2.get_yaxis().get_major_formatter().set_useOffset(False)

#ax3.plot(cProb,Desviacion_mochila_cProb,color='blue',label="Without Elitism")
#ax3.set_title('Standard Deviation')
#ax3.set_xlim(0.1,1)
#ax3.get_yaxis().get_major_formatter().set_useOffset(False)

#ax4.plot(cProb,Media_mochila_cProb,color='blue',label="Without Elitism")
#ax4.set_title('Medium value of the population')
#ax4.set_xlim(0.1,1)
#ax4.get_yaxis().get_major_formatter().set_useOffset(False)

ax1.plot(cProb,Accuracy_cProb_elitism,color='orange',label="With Elitism")
ax1.set_title('Accuracy')
ax1.set_xlim(0.1,1)
ax1.set_ylim(0,1.01)
ax1.get_yaxis().get_major_formatter().set_useOffset(False)

ax2.plot(cProb,Varianza_mochila_elitism,color='orange',label="With Elitism")
ax2.set_title('Variance')
ax2.set_xlim(0.1,1)
ax2.get_yaxis().get_major_formatter().set_useOffset(False)

ax3.plot(cProb,Desviacion_mochila_elitism,color='orange',label="With Elitism")
ax3.set_title('Standard Deviation')
ax3.set_xlim(0.1,1)
ax3.get_yaxis().get_major_formatter().set_useOffset(False)

ax4.plot(cProb,Media_mochila_elitism,color='orange',label="With Elitism")
ax4.set_title('Medium value of the population')
ax4.set_xlim(0.1,1)
ax4.get_yaxis().get_major_formatter().set_useOffset(False)

plt.legend()
plt.tight_layout()
plt.savefig('04.CrossoverProb_withElitism_behaviour.png')

Tournament_size =  [1, 3, 5, 7, 10]
Accuracy_Tournament_size_elitism =  [0.20800000000000002, 0.5500000000000002, 0.682, 0.74375, 0.7855999999999992]
Media_mochila_elitism =  [11401988.929198416, 12116065.293067463, 12396582.01800794, 12530414.540194446, 12609679.98158889]
Varianza_mochila_elitism =  [1942847519216.3662, 1103969422520.3, 774785747051.15, 612464115572.1277, 502693288710.53564]
Desviacion_mochila_elitism =  [1268416.376408458, 736734.463812609, 516999.86212056957, 422091.8597999657, 354256.9946142708]

fig, ((ax1, ax2),(ax3,ax4)) = plt.subplots(2,2)

ax1.plot(Tournament_size,Accuracy_Tournament_size,color='blue',label="Without Elitism")
ax1.set_title('Accuracy')
ax1.set_xlim(1,10)
ax1.set_ylim(0,1.01)
ax1.get_yaxis().get_major_formatter().set_useOffset(False)

#ax2.plot(Tournament_size,Varianza_mochila_tournamentSize,color='blue',label="Without Elitism")
#ax2.set_title('Variance')
#ax2.set_xlim(1,10)
#ax2.get_yaxis().get_major_formatter().set_useOffset(False)

#ax3.plot(Tournament_size,Desviacion_mochila_tournamentSize,color='blue',label="Without Elitism")
#ax3.set_title('Standard Deviation')
#ax3.set_xlim(1,10)
#ax3.get_yaxis().get_major_formatter().set_useOffset(False)

#ax4.plot(Tournament_size,Media_mochila,color='blue',label="Without Elitism")
#ax4.set_title('Medium value of the population')
#ax4.set_xlim(1,10)
#ax4.get_yaxis().get_major_formatter().set_useOffset(False)

ax1.plot(Tournament_size,Accuracy_Tournament_size_elitism,color='orange',label="With Elitism")
ax1.set_title('Accuracy')
ax1.set_xlim(1,10)
ax1.set_ylim(0,1.01)
ax1.get_yaxis().get_major_formatter().set_useOffset(False)
plt.legend()
ax2.plot(Tournament_size,Varianza_mochila_elitism,color='orange',label="With Elitism")
ax2.set_title('Variance')
ax2.set_xlim(1,10)
ax2.get_yaxis().get_major_formatter().set_useOffset(False)
plt.legend()
ax3.plot(Tournament_size,Desviacion_mochila_elitism,color='orange',label="With Elitism")
ax3.set_title('Standard Deviation')
ax3.set_xlim(1,10)
ax3.get_yaxis().get_major_formatter().set_useOffset(False)
plt.legend()
ax4.plot(Tournament_size,Media_mochila_elitism,color='orange',label="With Elitism")
ax4.set_title('Medium value of the population')
ax4.set_xlim(1,10)
ax4.get_yaxis().get_major_formatter().set_useOffset(False)

plt.legend()
plt.tight_layout()
plt.savefig('03.TournamentSize_withElitism_behaviour.png')








######################
###INVALID SOLS############
######################


mProb =  [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
Accuracy_mProb_elitism =  [0.8510000000000001, 0.7790000000000002, 0.6833333333333332, 0.5944999999999995, 0.5169999999999992, 0.45400000000000224, 0.4048571428571478, 0.36700000000000704, 0.33755555555556427, 0.31400000000001005]
Media_mochila_elitism =  [12829767.909174599, 12730450.430746034, 12558371.066133602, 12400815.628762899, 12267683.668796038, 12114184.071963636, 11985301.799603192, 11891257.239722727, 11777448.550314825, 11695474.040640492]
Varianza_mochila_elitism =  [279029835036.7612, 516718616881.8098, 799688462407.0823, 1058279307528.0038, 1252854781409.1133, 1441578442820.9468, 1607176111330.7285, 1699586456221.7402, 1853695963198.6423, 1986451689642.3694]
Desviacion_mochila_elitism =  [261997.00576621067, 438908.0534434483, 615554.4042852063, 762444.9737518745, 859812.3808296772, 952917.9366599501, 1032889.7419646612, 1084726.2538226563, 1147529.8375182587, 1195926.1332923558]

Accuracy_mProb_invalid =  [0.7710000000000001, 0.6759999999999995, 0.5843333333333324, 0.49774999999999836, 0.4325999999999978, 0.3838333333333306, 0.34671428571428253, 0.3182499999999965, 0.295333333333332, 0.2774000000000007]
Media_mochila_invalid =  [12542103.275329363, 12444438.33381349, 12315999.217006616, 12160347.886369048, 12006929.195567457, 11852441.02316402, 0, 0, 0, 0]
Varianza_mochila_invalid =  [594812628353.7206, 728841976517.24, 887525443872.6122, 1106519944181.3213, 1301293035378.1277, 1387819794139.12, 0, 0, 0, 0]
Desviacion_mochila_invalid =   [390871.23930928926, 539723.5403307865, 672906.4911206261, 791508.0612615524, 899294.4043548227, 952064.1991487201, 0, 0, 0, 0]



fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2)

ax1.plot(mProb,Accuracy_mProb,color='blue',label="Without Elitism")
ax1.set_title('Accuracy')
ax1.set_xlim(0.1,1)
ax1.set_ylim(0,1.01)
ax1.get_yaxis().get_major_formatter().set_useOffset(False)

ax2.plot(mProb,Varianza_mochila_mProb,color='blue',label="Without Elitism")
ax2.set_title('Variance')
ax2.set_xlim(0.1,1)
ax2.get_yaxis().get_major_formatter().set_useOffset(False)

ax3.plot(mProb,Desviacion_mochila_mProb,color='blue',label="Without Elitism")
ax3.set_title('Standard Deviation')
ax3.set_xlim(0.1,1)
ax3.get_yaxis().get_major_formatter().set_useOffset(False)

ax4.plot(mProb,Media_mochila_mProb,color='blue',label="Without Elitism")
ax4.set_title('Medium value of the population')
ax4.set_xlim(0.1,1)
ax4 .get_yaxis().get_major_formatter().set_useOffset(False)

ax1.plot(mProb,Accuracy_mProb_elitism,color='orange',label="With Elitism")
ax1.set_title('Accuracy')
ax1.set_xlim(0.1,1)
ax1.set_ylim(0,1.01)
ax1.get_yaxis().get_major_formatter().set_useOffset(False)

ax2.plot(mProb,Varianza_mochila_elitism,color='orange',label="With Elitism")
ax2.set_title('Variance')
ax2.set_xlim(0.1,1)
ax2.get_yaxis().get_major_formatter().set_useOffset(False)

ax3.plot(mProb,Desviacion_mochila_elitism,color='orange',label="With Elitism")
ax3.set_title('Standard Deviation')
ax3.set_xlim(0.1,1)
ax3.get_yaxis().get_major_formatter().set_useOffset(False)

ax4.plot(mProb,Media_mochila_elitism,color='orange',label="With Elitism")
ax4.set_title('Medium value of the population')
ax4.set_xlim(0.1,1)
ax4 .get_yaxis().get_major_formatter().set_useOffset(False)

ax1.plot(mProb,Accuracy_mProb_invalid,color='red',label="Start with invalid solutions")
ax1.set_title('Accuracy')
ax1.set_xlim(0.1,1)
ax1.set_ylim(0,1.01)
ax1.get_yaxis().get_major_formatter().set_useOffset(False)

ax2.plot(mProb,Varianza_mochila_invalid,color='red',label="Start with invalid solutions")
ax2.set_title('Variance')
ax2.set_xlim(0.1,1)
ax2.get_yaxis().get_major_formatter().set_useOffset(False)

ax3.plot(mProb,Desviacion_mochila_invalid,color='red',label="Start with invalid solutions")
ax3.set_title('Standard Deviation')
ax3.set_xlim(0.1,1)
ax3.get_yaxis().get_major_formatter().set_useOffset(False)

ax4.plot(mProb,Media_mochila_invalid,color='red',label="Start with invalid solutions")
ax4.set_title('Medium value of the population')
ax4.set_xlim(0.1,1)
ax4 .get_yaxis().get_major_formatter().set_useOffset(False)

plt.legend()
plt.tight_layout()
plt.savefig('05.MutationProb_withInvSols_behaviour.png')

nSolutions =  [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Accuracy_nSolutions_elitism =  [0.871, 0.8032499999999999, 0.7600555555555563, 0.7234166666666669, 0.691893333333333, 0.6529111111111102, 0.6092911564625847, 0.5709266369047614, 0.5414162698412701, 0.5099846428571426]
Media_mochila_elitism =  [12869428.0660754, 12883639.57303757, 12880157.064425468, 12893459.076801129, 12898273.945141127, 12901524.949750744, 12895669.764525883, 12879262.186147453, 12865400.052138263, 12850141.66628224]
Varianza_mochila_elitism =  [239400005694.7, 335273954458.48303, 451244429218.76556, 472349029850.3633, 499983415147.36115, 526239121721.14874, 552636843130.7808, 596147083236.9547, 638626689690.012, 669393400634.1884]
Desviacion_mochila_elitism = [197709.09489080834, 307677.7130839094, 425275.05554288375, 470832.12588512356, 517448.409948345, 552058.9598827102, 584343.600083545, 622965.0089249773, 658165.4515536464, 683380.980090186]

Accuracy_nSolutions_invalid =[0.8260000000000001, 0.7495000000000003, 0.6852222222222227, 0.6318541666666675, 0.5690033333333336, 0.5133916666666668, 0.473601020408164, 0.43715089285714354, 0.4010600529100543, 0.3758340476190483]  
Media_mochila_invalid = [12534001.641511906, 12598613.853934448, 12644891.503181085, 12660093.450164514, 12662439.469699325, 12656748.211911282, 12652005.748578226, 12634943.700850535, 12619466.885253789, 12601417.220452204] 
Varianza_mochila_invalid = [401095816730.1947, 471631549827.86835, 529140792519.77856, 581537412784.3455, 614142935891.153, 656819416542.94, 685101321045.5032, 725443137944.9198, 748116146475.1776, 780055071824.6001] 
Desviacion_mochila_invalid = [369419.3731432188, 456357.45460917085, 517178.0154764998, 569103.5124614997, 610761.391344188, 653948.3507073116, 684371.1684311554, 718162.4966437052, 741133.6740814213, 765736.6370535991]


fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2)

ax1.plot(nSolutions,Accuracy_nSolutions,color='blue',label="Without Elitism")
ax1.set_title('Accuracy')
ax1.set_xlim(10,100)
ax1.set_ylim(0,1.01)
ax1.get_yaxis().get_major_formatter().set_useOffset(False)

ax2.plot(nSolutions,Varianza_mochila_nSolutions,color='blue',label="Without Elitism")
ax2.set_title('Variance')
ax2.set_xlim(10,100)
ax2.get_yaxis().get_major_formatter().set_useOffset(False)

ax3.plot(nSolutions,Desviacion_mochila_nSolutions,color='blue',label="Without Elitism")
ax3.set_title('Standard Deviation')
ax3.set_xlim(10,100)
ax3.get_yaxis().get_major_formatter().set_useOffset(False)

ax4.plot(nSolutions,Media_mochila_nSolutions,color='blue',label="Without Elitism")
ax4.set_title('Medium value of the population')
ax4.set_xlim(10,100)
ax4 .get_yaxis().get_major_formatter().set_useOffset(False)

ax1.plot(nSolutions,Accuracy_nSolutions_elitism,color='orange',label="With Elitism")
ax1.set_title('Accuracy')
ax1.set_xlim(10,100)
ax1.set_ylim(0,1.01)
ax1.get_yaxis().get_major_formatter().set_useOffset(False)

ax2.plot(nSolutions,Varianza_mochila_elitism,color='orange',label="With Elitism")
ax2.set_title('Variance')
ax2.set_xlim(10,100)
ax2.get_yaxis().get_major_formatter().set_useOffset(False)

ax3.plot(nSolutions,Desviacion_mochila_elitism,color='orange',label="With Elitism")
ax3.set_title('Standard Deviation')
ax3.set_xlim(10,100)
ax3.get_yaxis().get_major_formatter().set_useOffset(False)

ax4.plot(nSolutions,Media_mochila_elitism,color='orange',label="With Elitism")
ax4.set_title('Medium value of the population')
ax4.set_xlim(10,100)
ax4 .get_yaxis().get_major_formatter().set_useOffset(False)

ax1.plot(nSolutions,Accuracy_nSolutions_invalid,color='red',label="Start with invalid solutions")
ax1.set_title('Accuracy')
ax1.set_xlim(10,100)
ax1.set_ylim(0,1.01)
ax1.get_yaxis().get_major_formatter().set_useOffset(False)

ax2.plot(nSolutions,Varianza_mochila_invalid,color='red',label="Start with invalid solutions")
ax2.set_title('Variance')
ax2.set_xlim(10,100)
ax2.get_yaxis().get_major_formatter().set_useOffset(False)

ax3.plot(nSolutions,Desviacion_mochila_invalid,color='red',label="Start with invalid solutions")
ax3.set_title('Standard Deviation')
ax3.set_xlim(10,100)
ax3.get_yaxis().get_major_formatter().set_useOffset(False)

ax4.plot(nSolutions,Media_mochila_invalid,color='red',label="Start with invalid solutions")
ax4.set_title('Medium value of the population')
ax4.set_xlim(10,100)
ax4 .get_yaxis().get_major_formatter().set_useOffset(False)

plt.legend()
plt.tight_layout()
plt.savefig('01.NSolutions_withInvSols_behaviour.png')

MaxGenerations_elitism =  [100, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 5000, 10000]
Accuracy_maxGenerations_elitism =  [0.855, 0.8675000000000003, 0.8610000000000004, 0.8662499999999995, 0.8745999999999992, 0.8748333333333314, 0.8688571428571404, 0.8723749999999972, 0.8716666666666641, 0.8729999999999971, 0.8674545454545426]
Media_mochila_elitism =  [12897423.459353175, 13008716.09800992, 13059214.447395502, 13099716.411322415, 13132992.87563571, 13145220.17081349, 13158913.216060663, 13170718.013931544, 13179920.959926363, 13188489.403706348, 13188509.008488096]
Varianza_mochila_elitism =  [345766992187.50836, 293223137195.9967, 261550201846.40616, 264645259633.37668, 240223117852.5757, 259997960150.25687, 256521679844.95932, 263660253057.02997, 261684670348.88412, 262697955589.10632, 280783065962.42145]
Desviacion_mochila_elitism =  [253681.61177215708, 235046.2107993938, 227457.71756610568, 226201.87798572966, 212546.43516303084, 230221.7348404713, 228529.9424954694, 230255.7414034404, 225955.51883575539, 224122.81752134353, 233700.38712752433]

Accuracy_maxGenerations_invalid = [0.8790000000000002, 0.8855000000000013, 0.8906666666666684, 0.8909999999999993, 0.8925999999999981, 0.8906666666666636, 0.8902857142857101, 0.8884999999999945, 0.8876666666666607, 0.8873999999999933, 0.8869090909090832] 
Media_mochila_invalid = [12924648.659460315, 13000965.474097224, 13054578.758759262, 13084338.371507935, 13117598.810778571, 13132737.183971561, 13148094.521517571, 13158833.08795982, 13169483.899083331, 13176650.406577775, 13189369.921684345] 
Varianza_mochila_invalid = [204535119002.87863, 305838436581.9877, 329314804428.3525, 362557421079.76337, 336924447975.12555, 353769399545.4676, 355153779472.75616, 364633402290.1853, 364891503302.45746, 382001196031.50555, 379805611781.1414] 
Desviacion_mochila_invalid =  [239116.53717448353, 297977.7349218721, 298773.9508707716, 309491.11779137165, 291371.63473768876, 299425.7584127414, 303868.70092272386, 309273.9886262107, 309837.9832653286, 317482.40093034925, 318357.9237311982]


fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2)

ax1.plot(MaxGenerations,Accuracy_maxGenerations, color='blue',label="Without Elitism")
ax1.set_title('Accuracy')
ax1.set_xlim(100,10000)
ax1.set_ylim(0,1.01)
ax1.get_yaxis().get_major_formatter().set_useOffset(False)

ax2.plot(MaxGenerations,Varianza_mochila_maxGenerations,color='blue',label="Without Elitism")
ax2.set_title('Variance')
ax2.set_xlim(100,10000)
ax2.get_yaxis().get_major_formatter().set_useOffset(False)

ax3.plot(MaxGenerations,Desviacion_mochila_maxGenerations,color='blue',label="Without Elitism")
ax3.set_title('Standard Deviation')
ax3.set_xlim(100,10000)
ax3.get_yaxis().get_major_formatter().set_useOffset(False)

ax4.plot(MaxGenerations,Media_mochila_maxGenerations,color='blue',label="Without Elitism")
ax4.set_title('Medium value of the population')
ax4.set_xlim(10,100)
ax4 .get_yaxis().get_major_formatter().set_useOffset(False)

ax1.plot(MaxGenerations,Accuracy_maxGenerations_elitism,color='orange',label="With Elitism")
ax1.set_title('Accuracy')
ax1.set_xlim(100,10000)
ax1.set_ylim(0,1.01)
ax1.get_yaxis().get_major_formatter().set_useOffset(False)

ax2.plot(MaxGenerations,Varianza_mochila_elitism,color='orange',label="With Elitism")
ax2.set_title('Variance')
ax2.set_xlim(100,10000)
ax2.get_yaxis().get_major_formatter().set_useOffset(False)

ax3.plot(MaxGenerations,Desviacion_mochila_elitism,color='orange',label="With Elitism")
ax3.set_title('Standard Deviation')
ax3.set_xlim(100,10000)
ax3.get_yaxis().get_major_formatter().set_useOffset(False)

ax4.plot(MaxGenerations,Media_mochila_elitism,color='orange',label="With Elitism")
ax4.set_title('Medium value of the population')
ax4.set_xlim(100,10000)
ax4 .get_yaxis().get_major_formatter().set_useOffset(False)

ax1.plot(MaxGenerations,Accuracy_maxGenerations_invalid,color='red',label="Start with invalid solutions")
ax1.set_title('Accuracy')
ax1.set_xlim(100,10000)
ax1.set_ylim(0,1.01)
ax1.get_yaxis().get_major_formatter().set_useOffset(False)

ax2.plot(MaxGenerations,Varianza_mochila_invalid,color='red',label="Start with invalid solutions")
ax2.set_title('Variance')
ax2.set_xlim(100,10000)
ax2.get_yaxis().get_major_formatter().set_useOffset(False)

ax3.plot(MaxGenerations,Desviacion_mochila_invalid,color='red',label="Start with invalid solutions")
ax3.set_title('Standard Deviation')
ax3.set_xlim(100,10000)
ax3.get_yaxis().get_major_formatter().set_useOffset(False)

ax4.plot(MaxGenerations,Media_mochila_invalid,color='red',label="Start with invalid solutions")
ax4.set_title('Medium value of the population')
ax4.set_xlim(100,10000)
ax4 .get_yaxis().get_major_formatter().set_useOffset(False)

plt.legend()
plt.tight_layout()
plt.savefig('02.MaxGenerations_withInvSols_behaviour.png')

cProb_eiltism =  [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
Accuracy_cProb_elitism =  [0.18499999999999983, 0.26750000000000024, 0.3716666666666663, 0.45024999999999954, 0.5005999999999998, 0.5401666666666665, 0.584, 0.6168749999999998, 0.6466666666666662, 0.6731999999999991]
Media_mochila_elitism =  [11643432.706805553, 11843504.554365074, 12028775.345701056, 12193832.873102183, 12283913.85535635, 12359813.962487433, 12429956.734607713, 12485529.733054573, 12528462.50220548, 12566836.685687708]
Varianza_mochila_elitism =  [910861346529.798, 928516422972.734, 859189244441.0999, 754097876953.2935, 734796159713.6248, 695670206600.0815, 641116532030.924, 589157294657.8583, 540335354758.0942, 506731406597.289]
Desviacion_mochila_elitism =  [666648.0145082935, 669236.3759606953, 618915.592536679, 554031.8150030642, 534755.6006553086, 506743.0109045006, 466994.64411077404, 436132.3456947148, 408293.59297071595, 384500.28080908203]

Accuracy_cProb_invalid =  [0.6550000000000002, 0.623, 0.6163333333333327, 0.6587499999999994, 0.6821999999999993, 0.6928333333333324, 0.7092857142857125, 0.7194999999999976, 0.7303333333333304, 0.740299999999996]


fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2)

ax1.plot(cProb,Accuracy_cProb,color='blue',label="Without Elitism")
ax1.set_title('Accuracy')
ax1.set_xlim(0.1,1)
ax1.set_ylim(0,1.01)
ax1.get_yaxis().get_major_formatter().set_useOffset(False)

#ax2.plot(cProb,Varianza_mochila_cProb,color='blue',label="Without Elitism")
#ax2.set_title('Variance')
#ax2.set_xlim(0.1,1)
#ax2.get_yaxis().get_major_formatter().set_useOffset(False)

#ax3.plot(cProb,Desviacion_mochila_cProb,color='blue',label="Without Elitism")
#ax3.set_title('Standard Deviation')
#ax3.set_xlim(0.1,1)
#ax3.get_yaxis().get_major_formatter().set_useOffset(False)

#ax4.plot(cProb,Media_mochila_cProb,color='blue',label="Without Elitism")
#ax4.set_title('Medium value of the population')
#ax4.set_xlim(0.1,1)
#ax4.get_yaxis().get_major_formatter().set_useOffset(False)

ax1.plot(cProb,Accuracy_cProb_elitism,color='orange',label="With Elitism")
ax1.set_title('Accuracy')
ax1.set_xlim(0.1,1)
ax1.set_ylim(0,1.01)
ax1.get_yaxis().get_major_formatter().set_useOffset(False)

ax2.plot(cProb,Varianza_mochila_elitism,color='orange',label="With Elitism")
ax2.set_title('Variance')
ax2.set_xlim(0.1,1)
ax2.get_yaxis().get_major_formatter().set_useOffset(False)

ax3.plot(cProb,Desviacion_mochila_elitism,color='orange',label="With Elitism")
ax3.set_title('Standard Deviation')
ax3.set_xlim(0.1,1)
ax3.get_yaxis().get_major_formatter().set_useOffset(False)

ax4.plot(cProb,Media_mochila_elitism,color='orange',label="With Elitism")
ax4.set_title('Medium value of the population')
ax4.set_xlim(0.1,1)
ax4.get_yaxis().get_major_formatter().set_useOffset(False)

ax1.plot(cProb,Accuracy_cProb_invalid,color='red',label="Start with invalid solutions")
ax1.set_title('Accuracy')
ax1.set_xlim(0.1,1)
ax1.set_ylim(0,1.01)
ax1.get_yaxis().get_major_formatter().set_useOffset(False)

plt.legend()
plt.tight_layout()
plt.savefig('04.CrossoverProb_withInvSols_behaviour.png')

Tournament_size =  [1, 3, 5, 7, 10]
Accuracy_Tournament_size_elitism =  [0.20800000000000002, 0.5500000000000002, 0.682, 0.74375, 0.7855999999999992]
Media_mochila_elitism =  [11401988.929198416, 12116065.293067463, 12396582.01800794, 12530414.540194446, 12609679.98158889]
Varianza_mochila_elitism =  [1942847519216.3662, 1103969422520.3, 774785747051.15, 612464115572.1277, 502693288710.53564]
Desviacion_mochila_elitism =  [1268416.376408458, 736734.463812609, 516999.86212056957, 422091.8597999657, 354256.9946142708]

Accuracy_Tournament_size_invalid = [0.05549999999999991, 0.3740000000000002, 0.5206666666666669, 0.600625, 0.6445999999999997] 
Media_mochila_invalid = [10316807.095896335, 11538940.10653071, 11961278.443787731, 12163587.535464216, 12285292.504494911] 
Varianza_mochila_invalid = [2628144692534.0723, 1599756473896.1797, 1234246026212.8496, 1050796799274.5808, 933139769258.4457] 
Desviacion_mochila_invalid = [1557100.40458041, 1055515.183087497, 868967.8146130943, 767829.6336595975, 708534.7035061439] 


fig, ((ax1, ax2),(ax3,ax4)) = plt.subplots(2,2)

ax1.plot(Tournament_size,Accuracy_Tournament_size,color='blue',label="Without Elitism")
ax1.set_title('Accuracy')
ax1.set_xlim(1,10)
ax1.set_ylim(0,1.01)
ax1.get_yaxis().get_major_formatter().set_useOffset(False)

#ax2.plot(Tournament_size,Varianza_mochila_tournamentSize,color='blue',label="Without Elitism")
#ax2.set_title('Variance')
#ax2.set_xlim(1,10)
#ax2.get_yaxis().get_major_formatter().set_useOffset(False)

#ax3.plot(Tournament_size,Desviacion_mochila_tournamentSize,color='blue',label="Without Elitism")
#ax3.set_title('Standard Deviation')
#ax3.set_xlim(1,10)
#ax3.get_yaxis().get_major_formatter().set_useOffset(False)

#ax4.plot(Tournament_size,Media_mochila,color='blue',label="Without Elitism")
#ax4.set_title('Medium value of the population')
#ax4.set_xlim(1,10)
#ax4.get_yaxis().get_major_formatter().set_useOffset(False)

ax1.plot(Tournament_size,Accuracy_Tournament_size_elitism,color='orange',label="With Elitism")
ax1.set_title('Accuracy')
ax1.set_xlim(1,10)
ax1.set_ylim(0,1.01)
ax1.get_yaxis().get_major_formatter().set_useOffset(False)
plt.legend()
ax2.plot(Tournament_size,Varianza_mochila_elitism,color='orange',label="With Elitism")
ax2.set_title('Variance')
ax2.set_xlim(1,10)
ax2.get_yaxis().get_major_formatter().set_useOffset(False)
plt.legend()
ax3.plot(Tournament_size,Desviacion_mochila_elitism,color='orange',label="With Elitism")
ax3.set_title('Standard Deviation')
ax3.set_xlim(1,10)
ax3.get_yaxis().get_major_formatter().set_useOffset(False)
plt.legend()
ax4.plot(Tournament_size,Media_mochila_elitism,color='orange',label="With Elitism")
ax4.set_title('Medium value of the population')
ax4.set_xlim(1,10)
ax4.get_yaxis().get_major_formatter().set_useOffset(False)

ax1.plot(Tournament_size,Accuracy_Tournament_size_invalid,color='red',label="Start with invalid solutions")
ax1.set_title('Accuracy')
ax1.set_xlim(1,10)
ax1.set_ylim(0,1.01)
ax1.get_yaxis().get_major_formatter().set_useOffset(False)
plt.legend()
ax2.plot(Tournament_size,Varianza_mochila_invalid,color='red',label="Start with invalid solutions")
ax2.set_title('Variance')
ax2.set_xlim(1,10)
ax2.get_yaxis().get_major_formatter().set_useOffset(False)
plt.legend()
ax3.plot(Tournament_size,Desviacion_mochila_invalid,color='red',label="Start with invalid solutions")
ax3.set_title('Standard Deviation')
ax3.set_xlim(1,10)
ax3.get_yaxis().get_major_formatter().set_useOffset(False)
plt.legend()
ax4.plot(Tournament_size,Media_mochila_invalid,color='red',label="Start with invalid solutions")
ax4.set_title('Medium value of the population')
ax4.set_xlim(1,10)
ax4.get_yaxis().get_major_formatter().set_useOffset(False)

plt.legend()
plt.tight_layout()
plt.savefig('03.TournamentSize_withInvSols_behaviour.png')