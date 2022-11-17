from typing import List
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

df = pd.read_csv('path/to/file/polls.csv')

def prepare() -> List[float]:
    """Returns a fragment of a table"""
    x = df[df["Fieldwork Period"] == "13 Sep 2022"].index.item()
    #print(x)
    y = df[df["Fieldwork Period"] == "2–7 Sep 2022"].index.item()
    #print(y)
    my_range = df.loc[x:y]
    #print(my_range)
    
    list_of_lists = []
    for column in my_range.columns[2:-13]:
        ith_column = my_range[column].astype(float).values.tolist()
        #print(ith_column)
        list_of_lists.append(ith_column)

    print(list_of_lists)
    return list_of_lists

def operations(i: float) -> List[float]:
    """Statistical operations"""
    mean = sum(i) / len(i)
    max_ = max(i)
    min_ = min(i)
    variance = np.var(i, ddof=1)
    st_dev = math.sqrt(variance)
    first_quantile = np.quantile(i, 0.25)
    median_ = np.quantile(i, 0.5)
    third_quantile = np.quantile(i, 0.75)
    iqr = third_quantile - first_quantile
    coe_var = st_dev / mean # [%]
    
    return [mean, max_, min_, variance, st_dev, first_quantile, median_, third_quantile, iqr, coe_var]

def combine():
    """Collects results into one list"""
    my_sum = [operations(i) for i in prepare()]
    print(my_sum)

    return my_sum

def insert():
    """Inserts data into a table"""
    list_of_parameters = combine()
    df = pd.DataFrame({"Parameters": ["Mean", "Max", "Min", "Variance", "St.dev", "First quantile", "Median", "Third quantile", "IQR", "Coe of Var"], "UR": list_of_parameters[0], "CC": list_of_parameters[1], "TL": list_of_parameters[2], "PC": list_of_parameters[3], "C": list_of_parameters[4], "P2050": list_of_parameters[5]})
    print(df)

    return df

def visualize():
    """Visualizes data in matplotlib. In this case it's the arithmetic mean"""
    results = combine()
    names_of_parties = ["UR", "CC", "TL", "PC", "C", "PL2050"]
    display_list = []
    for x in range(0, 6):
        res3 = results[x][1]
        display_list.append(res3)
        #print(res3)

    print(display_list)

    plt.bar(range(len(names_of_parties)), display_list)
    
    plt.ylabel("Results")
    plt.title("Table")
    plt.xticks(range(len(names_of_parties)), names_of_parties)

    plt.show()

visualize()
