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

Prerequisites:
Python 3.8.1
pandas
numpy
csv
sklearn
