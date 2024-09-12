import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split

data = pd.read_csv('https://raw.githubusercontent.com/DataThinkers/Datasets/main/DS/water_potability.csv', sep=',')

train_data, test_data = train_test_split(data,  test_size=.25, random_state=42)


data_path = os.path.join("data","raw")

os.makedirs(data_path)

train_data.to_csv(os.path.join(data_path, 'train.csv'),index=False)
test_data.to_csv(os.path.join(data_path, 'test.csv'),index=False)
