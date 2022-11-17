from typing import List
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.stats import kurtosis

df = pd.read_csv('./polls19_date.csv')

def prepare() -> List[float]:
    """Returns a fragment of a table""" 
    list_of_lists = []

    for column in df.columns[2:8]:
        ith_column = df[column].astype(float).values.tolist()
        list_of_lists.append(ith_column)
    
    return list_of_lists

def operations(i: float) -> List[float]:
    """Statistical operations"""
    mean = sum(i) / len(i)
    max_ = max(i)
    min_ = min(i)
    variance = np.var(i)
    st_dev = math.sqrt(variance)
    first_quantile = np.quantile(i, 0.25)
    median_ = np.quantile(i, 0.5)
    third_quantile = np.quantile(i, 0.75)
    iqr = third_quantile - first_quantile
    coe_var = st_dev / mean
    kurtosis_ = kurtosis(i)
    
    list_of_results = [mean, max_, min_, variance, st_dev, first_quantile, median_, third_quantile, iqr, coe_var, kurtosis_]
    r_list_of_res = [round(x, 2) for x in list_of_results]

    return r_list_of_res

def combine():
    """Collects results into one list"""
    my_sum = [operations(i) for i in prepare()]

    return my_sum

def insert():
    """Inserts data into a table"""
    list_of_parameters = combine()

    df = pd.DataFrame({"Parameters": ["Mean", "Max", "Min", "Variance", "St.dev", "First quantile", "Median", "Third quantile", "IQR", "Coe of Var", "Kurtosis"], "UR": list_of_parameters[0], "CC": list_of_parameters[1], "TL": list_of_parameters[2], "PC": list_of_parameters[3], "C": list_of_parameters[4], "PL2050": list_of_parameters[5]})
    #print(df)

    df.to_csv('./report.csv', index=False)

    return df

insert()
