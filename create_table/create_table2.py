import pandas as pd
from typing import List

df = pd.read_csv('path/to/file/polls.csv')

#creates a new table from a fragment of a larger table
def prepare() -> List[float]:
    """Returns a fragment of a table"""
    x = df[df["Fieldwork Period"] == "5–15 Sep 2022"].index.item() # note that... "–" is different than "-"
    y = df[df["Fieldwork Period"] == "13–14 Sep 2021"].index.item()
    
    my_range = df.loc[x:y]
    
    list_of_lists = []
    for column in my_range.columns[2:-13]:
        ith_column = my_range[column].astype(float).values.tolist()
        #print(ith_column)
        list_of_lists.append(ith_column)

    print(list_of_lists)
    return list_of_lists

def combine():
    lists = prepare()
    
    df2 = pd.DataFrame({"United Right": lists[0], "Civic Coalition": lists[1], "The Left": lists[2], "Polish Coalition": lists[3], "Confederation": lists[4], "Poland 2050": lists[5]})
    print(df2)
    
    df2.to_csv('path/to/file/all_parties.csv', index=False)

combine()
