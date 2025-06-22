import requests
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px

# ---------------------
# 1. Fetch API Data
# ---------------------
url = "https://api.rootnet.in/covid19-in/stats/latest"
response = requests.get(url)
data = response.json()

regional_data = data['data']['regional']
df = pd.DataFrame(regional_data)

# Rename columns
df = df.rename(columns={
    'loc': 'State',
    'confirmedCasesIndian': 'Indian Cases',
    'confirmedCasesForeign': 'Foreign Cases',
    'totalConfirmed': 'Total Cases',
    'discharged': 'Recovered',
    'deaths': 'Deaths'
})

df = df.sort_values(by='Total Cases', ascending=False)
top10 = df.head(10)

# ---------------------
# 2. Create Subplot Dashboard
# ---------------------

from plotly.subplots import make_subplots

# Define subplot layout (2 rows x 3 columns)
fig = make_subplots(
    rows=3, cols=2,
    subplot_titles=(
        "BarChart: Total Cases per State",
        "PieChart: Top 10 States Affection Percentage",
        "BoxPLot: Total Cases, Recovered, Deaths",
        "Histogram: Total Cases",
        "LineGraph: Total Cases by State",
        ""
    ),
    specs=[
        [{"type": "bar"}, {"type": "pie"}],
        [{"type": "box"}, {"type": "xy"}],
        [{"type": "scatter"}, None]
    ],
    vertical_spacing=0.19,
    horizontal_spacing=0.15)

# --- Bar Chart ---
fig.add_trace(
    go.Bar(x=df['State'], y=df['Total Cases'], marker_color='red', name="Total Cases"),
    row=1, col=1
)

# --- Pie Chart ---
fig.add_trace(
    go.Pie(labels=top10['State'], values=top10['Total Cases'], name="Top 10 States Affection Percentage"),
    row=1, col=2
)

# --- Box Plot ---
fig.add_trace(go.Box(y=df['Total Cases'], name='Total Cases'), row=2, col=1)
fig.add_trace(go.Box(y=df['Recovered'], name='Recovered'), row=2, col=1)
fig.add_trace(go.Box(y=df['Deaths'], name='Deaths'), row=2, col=1)

# --- Histogram ---
fig.add_trace(
    go.Histogram(x=df['Total Cases'], nbinsx=15, name="Total Cases Distribution"),
    row=2, col=2
)

# --- Line Chart ---
fig.add_trace(
    go.Scatter(x=df['State'], y=df['Total Cases'], mode='lines+markers', name="Line Chart"),row=3, col=1
)

# ---------------------
# 3. Final Layout Adjustments
# ---------------------

fig.update_layout(
   title=dict(
        text="<b>COVID-19 DASHBOARD FOR INDIA</b>",  
        font=dict(
            family="Times New Roman",  
            size=37,
            color="darkblue"           
        ),
        x=0.5,  
        xanchor='center'
    ),
    font=dict(
        family="Times New Roman",  
        size=16,
        color="black"
    ),
    height=1500,
    width=1000,
    showlegend=False,
    colorway=px.colors.qualitative.Plotly,
    margin=dict(t=180, b=200, l=50, r=50)  
)
for annotation in fig['layout']['annotations']:
    annotation['font'] = dict(size=19, family='Times New Roman', color='black',weight='bold') 

fig.show()
