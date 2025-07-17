import base64
import io
import dash
from dash import dcc, html, Input, Output, State
import plotly.graph_objs as go
import pandas as pd
import numpy as np

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Upload(
        id='upload-data',
        children=html.Button('Przeglądaj i załaduj CSV'),
        multiple=False
    ),
    dcc.Graph(id='3d-plot')
])

def parse_contents(contents):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    return pd.read_csv(io.StringIO(decoded.decode('utf-8')))

@app.callback(
    Output('3d-plot', 'figure'),
    Input('upload-data', 'contents')
)
def update_output(contents):
    if contents is None:
        # pusty wykres na start
        fig = go.Figure()
        fig.update_layout(title='Wczytaj plik CSV')
        return fig

    df = parse_contents(contents)

    # Załóżmy, że CSV ma kolumny: x, y, z
    fig = go.Figure(data=[go.Scatter3d(
        x=df['x'], y=df['y'], z=df['z'],
        mode='markers',
        marker=dict(size=5, color=df['z'], colorscale='Viridis', opacity=0.8)
    )])
    fig.update_layout(margin=dict(l=0, r=0, b=0, t=30), title='Interaktywny wykres 3D')
    return fig

if __name__ == '__main__':
    app.run(debug=True)