from predictions.prediction import Predict
import pandas as pd
import numpy as np

from utilities.utils import TweakPadResultData

"""
data:
    domain
    product
    cost,
    age,
    income,
    gender,
    education
"""


def data_loader(data):
    return pd.read_csv(
        f"data/{data.get('category').lower()}/{data.get('product').lower()}"
    )


def model_graph(data):
    df = data_loader(data)
    prediction = []
    features = []
    for i in range(len(df)):
        features.append(i)
        data["age"] = df["age"][i]
        data["income"] = df["monthly_income"][i]
        data["gender"] = df["gender"][i]
        data["education"] = df["education"][i]
        pred_obj = TweakPadResultData(data)
        if pred_obj["binary"] == 0:
            prediction.append(1 - pred_obj["probability"])
        else:
            prediction.append(pred_obj["probability"])
    actual = df["purchased"]

    result = {"features": features, "prediction": prediction, "actual": actual}

    return actual
