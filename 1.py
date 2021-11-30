import plotly.graph_objects as go
import pandas as pd
from datetime import datetime
# csv file name
filename = "./ETHUSDC_1.csv"

df = pd.read_csv(filename)


startdate = 1578505380
enddate = 1583942580
anus = df[df["Timestamp"] < enddate]

print(anus)
fig = go.Figure(data=[go.Candlestick(x=anus['Timestamp'],
                open=anus['Open'],
                high=anus['High'],
                low=anus['Low'],
                close=anus['Close'])])

fig.show()