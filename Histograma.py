import plotly.graph_objects as go
import numpy as np

x0 = np.random.randn(500)
x1 = np.random.randn(500)+2

fig = go.Figure()
fig.add_trace(go.Histogram(x=x0))
fig.add_trace(go.Histogram(x=x1))

fig.update_layout(barmode='overlay')

fig.update_traces(opacity = 0.80)

fig.show()
