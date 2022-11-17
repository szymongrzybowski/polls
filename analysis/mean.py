import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('./polls19_date.csv')

list_of_columns = []
for column in df.columns[2:8]:
    ith_column = df[column].astype(float).values.tolist()
    list_of_columns.append(ith_column)

list_of_means = []
for e in list_of_columns:
    mean = sum(e) / len(e)
    rounded = round(mean, 2)
    list_of_means.append(rounded)

names_of_parties = ["UR", "CC", "TL", "PC", "C", "PL2050"]
c = ["darkblue", "orange", "red", "green", "black", "yellow"]

plt.bar(range(len(list_of_means)), list_of_means, color=c)
plt.title("Mean Comparison; Oct 2019 – 5 Nov 2022")
plt.ylabel("Results")

plt.xticks(range(len(names_of_parties)), names_of_parties)

plt.show()
