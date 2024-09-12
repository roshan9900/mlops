from fastapi import FastAPI
import pickle
import pandas as pd

app = FastAPI(
    title = "Water Potability Prediction",
    description="Predicting Water Potability"
)

with open(r"C:\Users\admin\Downloads\MlOps\project\model.pkl",'rb') as f:
    model = pickle.load(f)
    
@app.get("/")
def index():
    return "welcome to water potability prediction"



