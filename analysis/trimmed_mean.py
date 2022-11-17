from scipy.stats import trim_mean
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv('./polls19_date.csv')

list_of_columns = []
for col in df.columns[2:8]:
    ith_column = df[col].astype(float).values.tolist()
    list_of_columns.append(ith_column)

res_list = []
for i in list_of_columns:
    res = trim_mean(i, 0.25)
    res_list.append(res)

names_of_parties = ["UR", "CC", "TL", "PC", "C", "PL2050"]
c = ["darkblue", "orange", "red", "green", "black", "yellow"]

plt.bar(range(len(res_list)), res_list, color=c)
plt.title("Trimmed Mean Comparison; Oct 2019 – 5 Nov 2022")
plt.ylabel("Results")

plt.xticks(range(len(names_of_parties)), names_of_parties)

plt.show()
