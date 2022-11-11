import plotly.graph_objects as go
from valores import *
numbers = Valores

fig = go.Figure()
fig.add_trace(go.Histogram(x=numbers, name = "count", texttemplate="%{x}", textfont_size=20))

fig.show()