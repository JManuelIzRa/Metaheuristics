import pandas as pd
import matplotlib.pyplot as plt

pd.set_option("display.precision",2)

df = pd.read_csv('data\output_SimAnnealing.csv')

print(df.columns)

init1 = []
init2 = []
init3 = []
init4 = []
cities = [5,6,7,10,15,20,30,50,75,100,150]
time = []
length = []

for city in cities:
    
    # It calculates the mean of the time and for every city amd
    # store it in a list
    init1.append(df[ (df["N Cities"] == city) & (df["Initial Ta"] == 1)]["Time"].mean())
    init3.append(df[ (df["N Cities"] == city) & (df["Initial Ta"] == 10)]["Time"].mean())

    #length.append(df[df["N Cities"] == city]["Length"].mean())


fig, ax = plt.subplots()

# ax.plot(cities,length, cities, time) To combine diagrams

ax.plot(cities,init1,label='Ta Inicial = 1')
ax.plot(cities,init3,label='Ta Inicial = 10')

ax.set_xlim(0, 150)
ax.set_xlabel('Nº of Cities')
ax.set_ylabel('Time')

plt.legend()

plt.show()