import pandas as pd
from typing import List

df = pd.read_csv('path/to/file/german_polls.csv')

def prepare() -> List[float]:
    """Returns a fragment of a table"""
    x = df['SPD'].astype(float).values.tolist()
    y = df['Union'].astype(float).values.tolist()
    
    return [x, y]

def combine():
    lists = prepare()
    
    df2 = pd.DataFrame({"SPD": lists[0], "Union": lists[1]})
    print(df2)
    
    df2.to_csv('path/to/file/spd_union.csv', index=False)

combine()
