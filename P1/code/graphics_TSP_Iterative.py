import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.set_option("display.precision",2)

df = pd.read_csv('..\data\output_iterated_local_search.csv')

print(df.columns)

df["Time"] = df["Time"].astype("float64")


cities = [5,6,7,15,20,30,50,75,100,150]
iterations = [1,10,100]
time = []
length = []

counter = 0

x1 = df[ (df["N Cities"] == 5)]["Time"]
x2 = df[ (df["N Cities"] == 6)]["Time"]
x3 = df[ (df["N Cities"] == 7)]["Time"]
x4 = df[ (df["N Cities"] == 15)]["Time"]
x5 = df[ (df["N Cities"] == 20)]["Time"]
x6 = df[ (df["N Cities"] == 30)]["Time"]
x7 = df[ (df["N Cities"] == 50)]["Time"]
x8 = df[ (df["N Cities"] == 75)]["Time"]
x9 = df[ (df["N Cities"] == 100)]["Time"]
x10 = df[ (df["N Cities"] == 150)]["Time"]

fig, ax = plt.subplots()

ax.plot(x1, iterations, label= '5 cities')
ax.plot(x2, iterations, label= '6 cities')
ax.plot(x3, iterations, label= '7 cities')
ax.plot(x4, iterations, label= '15 cities')
ax.plot(x5, iterations, label= '20 cities')
ax.plot(x6, iterations, label= '30 cities')
ax.plot(x7, iterations, label= '50 cities')
ax.plot(x8, iterations, label= '75 cities')
ax.plot(x9, iterations, label= '100 cities')
ax.plot(x10, iterations, label= '150 cities')# To combine diagrams

#ax.plot(cities,timeb)

#ax.set_xlim(0, 150)
ax.set_xlabel('Time')
ax.set_ylabel('Iterations')

plt.legend()

plt.show()