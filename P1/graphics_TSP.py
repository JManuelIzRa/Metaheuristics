import pandas as pd
import matplotlib.pyplot as plt

pd.set_option("display.precision",2)

df = pd.read_csv('data\output_SimAnnealing.csv')

print(df.columns)


cities = [5,6,7,10,15,20,30,50,75,100,150]
time = []
length = []

for city in cities:
    
    # It calculates the mean of the time and for every city amd
    # store it in a list
    time.append(df[df["N Cities"] == city]["Time"].mean())

    length.append(df[df["N Cities"] == city]["Length"].mean())


fig, ax = plt.subplots()

# ax.plot(cities,length, cities, time) To combine diagrams

ax.plot(cities,length)

ax.set_xlim(0, 150)
ax.set_xlabel('Nº of Cities')
ax.set_ylabel('Length')

plt.show()