import pandas as pd
from data.data import *

def characters(df: pd.DataFrame) -> None:
    print(df)

if __name__ == '__main__':
    df = pd.DataFrame(data)
    characters(df)