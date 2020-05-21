import pandas as pd
diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
print("Original Dataframe:")
print(diamonds.shape)
print("\nSample 75% of diamonds DataFrame's rows without replacement:")
result = diamonds.sample(frac=0.75, random_state=99)
print(result)
print("\nRemaining 25% of the rows:")
print(diamonds.loc[~diamonds.index.isin(result.index), :])