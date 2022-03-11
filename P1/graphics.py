import pandas as pd
import matplotlib.pyplot as plt

pd.set_option("display.precision",2)

df = pd.read_csv('data\output_SimAnnealing_Logarithmic.csv')

print(df.columns)

init1 = []
init2 = []
init3 = []
init4 = []
cities = [5,6,7,10,15,20,30,50,75,100,150]
time = []
length = []

stop_criteria = [0.05,0.1,0.25,0.5,0.75,0.99]

for city in cities:
    
    # It calculates the mean of the time and for every city amd
    # store it in a list
    init1.append(df[df["N Cities"] == city]["Time"].mean())
    
    #length.append(df[df["N Cities"] == city]["Length"].mean())


fig, ax = plt.subplots()

# ax.plot(cities,length, cities, time) To combine diagrams

ax.plot(cities,init1)



ax.set_xlim(0, 150)
ax.set_xlabel('Nº Cities')
ax.set_ylabel('Time')

plt.show()