import pandas as pd
import numpy as np
import os
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import json 

test_data = pd.read_csv('./data/processed/test_processed.csv')


x_test = test_data.iloc[:,0:-1].values
y_test = test_data.iloc[:,-1].values

model = pickle.load(open('model.pkl','rb'))

pred = model.predict(x_test)

accuracy = accuracy_score(y_test, pred)
precission = precision_score(y_test, pred)
recall = recall_score(y_test, pred)
f1score = f1_score(y_test, pred)

metrics_dict = {
    'acc':accuracy,
    'precission':precission,
    'recall':recall,
    'f1score':f1score
}

with open('metrics.json','w') as file:
    json.dump(metrics_dict, file, indent=4)