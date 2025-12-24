import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    filterdf = animals.loc[animals['weight'] > 100]
    filterdf = filterdf.sort_values(by='weight', ascending=False)
    filterdf = filterdf.iloc[:,[0]]
    return filterdf