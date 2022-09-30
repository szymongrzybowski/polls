import pandas as pd
from typing import List

df = pd.read_csv('path/to/file/polls.csv')

#creates a new table from a fragment of a larger table
def prepare() -> List[float]:
    """Returns a fragment of a table"""
    x = df[df["Fieldwork Period"] == "5–15 Sep 2022"].index.item() # note that... "–" is different than "-"
    y = df[df["Fieldwork Period"] == "13–14 Sep 2021"].index.item()
    
    my_range = df.loc[x:y]
    
    first_col = my_range.iloc[:, 7].astype(float).values.tolist()
    #print(first_col)
    second_col = my_range.iloc[:, 6].astype(float).values.tolist()
    #print(second_col)

    #print(list_of_lists)
    return [first_col, second_col]

def combine():
    lists = prepare()
    
    df2 = pd.DataFrame({"Poland 2050": lists[0], "Confederation": lists[1]})
    print(df2)
    
    df2.to_csv('path/to/file/pl2050_c.csv', index=False)

combine()
