Implementation of regression models and analysis of polls in Europe. Currently, the repository covers Poland and Germany. [Work in progress]

The repository consists of:
- statistics.py: selects fragment of the dataset, performs descriptive statistics operations, inserts results into df, visualizes data in matplotlib.
- corr.py: calculates correlation coefficient and visualizes it in matplotlib.
- polls.csv: dateset containing polls results from Poland. It covers period since 11.2015 until now.
- german_polls.csv: dataset containing polls from Germany. Since 2021 federal elections until now. 
- lin_reg.py: Linear Regression
- poly_reg.py: Polynomial Regression
- multi_linreg.py: Multiple (Linear) Regression
- svr.py: Support Vector Regression
- create_table: Python scripts which select columns from dataset and save them to another csv file.
- spd_union.csv: pair of columns (SPD and Union parties (DE))
- ur_cc.csv: pair of columns (United Right and Civic Coalition parties (PL))
- cc_tl.csv pair of columns (Civic Coalition and The Left (PL))
- comparison.png: chart comparing Correlation Coe. of two leading parties of Germany with two main Polish parties.

Prerequisites:
- Python 3.8.1
- pandas
- numpy
- csv
- sklearn

![comparison_ger_pl](https://user-images.githubusercontent.com/63613188/193253971-0ae9b6b5-79f9-41a3-94dc-62ce93dfe17b.png)
