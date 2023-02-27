
import numpy as np
import pandas as pd

def generate_data():
    df = pd.read_csv("Data/anime_cleaned.csv")
    df = df[['score','popularity','genre']]
    df['split'] = np.random.randn(df.shape[0], 1)
    msk = np.random.rand(len(df)) <= 0.7
    train = df[msk]
    test = df[~msk]
    train = train[['score','popularity','genre']]
    test = test[['score','popularity','genre']]
    train.to_csv("Data/training.csv")
    test.to_csv("Data/test.csv")
def main():
    generate_data()

main()
    