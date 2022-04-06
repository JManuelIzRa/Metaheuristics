import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

pd.set_option("display.precision",2)

df = pd.read_csv("../data/knapsack_item_increment_behaviour.csv")

print(df.columns)


n_items = [5,6,7,8,10,15,24]

acc = []

for number in n_items:

    acc.append(df[ (df["N Items"] == number)]["Accuracy"].mean())



fig, ax = plt.subplots()

ax.plot(n_items,acc)
ax.set_xlim(5,24)
ax.set_ylim(0.6,0.8)
ax.set_xlabel('N Items')
ax.set_ylabel('Accuracy')


plt.savefig('00.accuracy_items_change.png')

correlation, p_value = stats.pearsonr(n_items, acc)

print("La relacion entre ambas variables es de ",correlation)
print("Con una certeza de ", 1-p_value)