import pandas as pd

df = pd.read_csv(
    "/home/jigar/Projects/Advertisement Analysis/Ads-Analysis-Deployed/Advertisement-Analysis-backend/data/automobile/bike.csv"
)

for i in range(0, len(df)):
    try:
        if int(df["monthly_income"][i]) < 10:
            df["monthly_income"][i] = 10
            print("888888888888888888888888888 flag")
        elif int(df["monthly_income"][i]) > 200:
            df["monthly_income"][i] = 200
            print("########################## flag")

        # df["monthly_income"][i] = int(df["monthly_income"][i])
        # df["sex"][i] = 1 if df["sex"][i].lower() == "male" else 0
        # df["age"][i] = int(df["age"][i])
        # df["education"][i] = int(df["education"][i])
        # df["purchased"][i] = int(df["purchased"][i])
        # df["product"][i] = int(df["product"][i])

        if df["sex"][i].lower() == "male":
            df["sex"][i] = 1
        else:
            df["sex"][i] = 0

        if int(df["monthly_income"][i]) > 100:
            df["quality"][i] = 1
            print("Changed")
        df["quality"][i] = int(df["quality"][i])
    
    except Exception as e:
        pass


df.to_csv(
    "/home/jigar/Projects/Advertisement Analysis/Ads-Analysis-Deployed/Advertisement-Analysis-backend/data/automobile/bike.csv"
)
