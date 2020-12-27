import pandas as pd

df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
df_colors = df["Primary Fur Color"].unique()[1:]
dict_to_convert = {key: len(df[df["Primary Fur Color"] == key]) for key in df_colors}


new_df = pd.DataFrame({"Fur Color": dict_to_convert.keys(), "Count": dict_to_convert.values()})
new_df.to_csv("new_df.csv")
