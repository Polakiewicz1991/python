import plotly.graph_objs as go

def create_3d_scatter(df):
    scatter = go.Scatter3d(
        x=df['x'].values,
        y=df['y'].values,
        z=df['z'].values,
        mode='markers',
        marker=dict(
            size=5,
            color=df['z'].values,      # jednowymiarowa tablica liczb
            colorscale='Viridis',
            opacity=0.8,
            colorbar=dict(title='Z value')
        )
    )
    fig = go.Figure(data=[scatter])  # <-- tu musi być lista trace'ów w data!
    fig.update_layout(
        margin=dict(l=0, r=0, b=0, t=40),
        scene=dict(
            xaxis_title='X',
            yaxis_title='Y',
            zaxis_title='Z'
        ),
        title='Interaktywny wykres 3D'
    )
    return fig