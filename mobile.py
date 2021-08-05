import csv
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("Mobile.csv")

fig = go.Figure(go.Bar(
    x = ["Avg Rating"],
    y = ["Mobile Brand"],
    ))

fig.show()