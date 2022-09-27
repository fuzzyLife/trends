import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("df.csv")
plt.barh(df['disease'], df['value'])
plt.title("Rising", size=18)
plt.savefig("map.png", bbox_inches="tight")
#https://github.com/GeneralMills/pytrends?ref=hackernoon.com#top-charts
#data['disease']['top']
