import pandas as pd
import plotly.graph_objects as go

prices = [
	(1, 2.12),
	(2, 2.56),
	(3, 3.10),
	(4, 3.16),
	(5, 3.58),
	(6, 5.12),
	(7, 5.16),
	(8, 5.20),
	(9, 4.12),
	(10, 4.10),
	(11, 3.65),
	(12, 4.25),
]

df = pd.DataFrame(prices, columns=["month", "pricePLN"])

df.set_index("month", inplace=True)

df["priceUSD"] = df["pricePLN"] / 4

fig = go.Figure()
fig.add_trace(go.Scatter(x=df.index, y=df['priceUSD'], mode='lines', line=dict(color='red', dash='dash')))

fig.update_layout(title='Prices in USD over months', xaxis_title='Month', yaxis_title='Price in USD')
fig.show()