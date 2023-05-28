import plotly.graph_objects as go

salaries = [
    ("Mark", 1000),
    ("John", 1500),
    ("Daniel", 2300),
    ("Greg", 5000)
]

names = [name for name, _ in salaries]
salary_values = [salary for _, salary in salaries]

fig = go.Figure(data=go.Bar(x=names, y=salary_values))

fig.update_layout(title_text='Salaries Bar Chart', xaxis_title="Names", yaxis_title="Salary")

fig.show()