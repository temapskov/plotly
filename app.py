import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


df = pd.read_csv("foo.txt", sep=",", header=None, 
                 names=["date", "plot", "name", "val"])
df1 = df.groupby("plot", as_index=False)

config = dict(
    {'scrollZoom': True,
     'modeBarButtonsToRemove': ['zoom', 'pan'],
     'displaylogo': False
    })

i = 0
fig = make_subplots(rows=len(df1), cols=2)
for group in df1:
    for test, group in df1.get_group(i).groupby(["name"], as_index=False):
        fig.add_trace(
        go.Scatter(
            {'x': group['date'], 
             'y': group['val'],
             'name': test,
            }), 
             row=i+1, col=1)
    i =+ 1

fig.update_layout(xaxis = {'type': 'date'})

fig.show(config=config)
