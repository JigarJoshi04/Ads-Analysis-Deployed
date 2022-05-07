import pandas as pd

df = pd.read_csv(
    "/home/jigar/Projects/Advertisement Analysis/Ads-Analysis-Deployed/Advertisement-Analysis-backend/data/automobile/car.csv"
)

for i in range(0, len(df)):
    if int(df["monthly_income"][i]) < 10:
        df["monthly_income"][i] = 10
        print("888888888888888888888888888 flag")
    elif int(df["monthly_income"][i]) > 200:
        df["monthly_income"][i] = 200
        print("########################## flag")

    df["monthly_income"][i] = int(df["monthly_income"][i])
    df["sex"][i] = 1 if df["sex"][i].lower() == "male" else 0
    df["age"][i] = int(df["age"][i])
    df["education"][i] = int(df["education"][i])
    df["purchased"][i] = int(df["purchased"][i])
    df["product"][i] = int(df["product"][i])
    df["quality"][i] = int(df["quality"][i])

df.to_csv(
    "/home/jigar/Projects/Advertisement Analysis/Ads-Analysis-Deployed/Advertisement-Analysis-backend/data/automobile/car.csv"
)
