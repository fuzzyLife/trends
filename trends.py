#https://hackernoon.com/how-to-use-google-trends-api-with-python
import pandas as pd
from pytrends.request import TrendReq
pytrend = TrendReq()
pytrend.build_payload(kw_list=["Disease"], timeframe='now 1-d')#,geo='', gprop='', cat=0) 
# ## Related Topics 
df_related_topics = pytrend.related_topics()['Disease']['rising']
#df_related_topics=df_related_topics[df_related_topics['topic_type'].isin(['Disorder', 'Diseases'])]
df_related_topics=df_related_topics[['topic_title','value']]
df_related_topics['value']=0
# ## Related Queries
df_related_queries = pytrend.related_queries()['Disease']['top']
df=pd.concat([df_related_queries, df_related_topics], ignore_index=True)
#merge
df_related_topics.columns=df_related_queries.columns
df=pd.concat([df_related_queries, df_related_topics], ignore_index=True)
df = df.sort_values('value', ascending=True)
df['disease'] = df['query'].str.split().str.join(' ')
df['disease'] = df['disease'].str.lower()
df['disease'] = df['disease'].str.replace('diseases', '')
df['disease'] = df['disease'].str.replace('disease', '')
df['disease'] = df['disease'].str.strip()
#data = pytrends.interest_over_time() 
#data = data.reset_index() 
#data.save("data.csv")
#import plotly.express as px
#fig = px.line(data, x="date", y=['disease'], title='Keyword Web Search Interest Over Time')
#fig.show() 
#plt.scatter(data["date"],data['disease'], title='Keyword Web Search Interest Over Time')
#pytrends.get_historical_interest(kw_list, year_start=2021, month_start=9, day_start=1, hour_start=0, year_end=2021, month_end=9, day_end=30, hour_end=0, cat=0, sleep=0)
#by_region = pytrends.interest_by_region(resolution='COUNTRY', inc_low_vol=True, inc_geo_code=False)
#by_region.head(10) 
#df_reg=by_region[by_region["disease"] > 50]
#df_reg= df_reg.sort_values('disease')
#df_reg.to_csv("df_reg.csv")
#df_reg.plot(kind="barh").figure.savefig("mapreg.png",dpi=100,bbox_inches = "tight")
#df.plot(kind="barh").figure.savefig("mapV.png",dpi=100,bbox_inches = "tight")
df.to_csv("df.csv")
import matplotlib.pyplot as plt
plt.barh(df['disease'],df['value'])
plt.title("Rising", size=18)
plt.savefig("map.png",bbox_inches = "tight")
#https://github.com/GeneralMills/pytrends?ref=hackernoon.com#top-charts
#data['disease']['top'] 
