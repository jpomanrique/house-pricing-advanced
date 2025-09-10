import pandas as pd
from sklearn.model_selection import train_test_split

def load_and_split_data(path):
    df = pd.read_csv(path)
    X = df.drop('SalePrice', axis=1)
    y = df['SalePrice']
    return train_test_split(X, y, test_size=0.2, random_state=42)
