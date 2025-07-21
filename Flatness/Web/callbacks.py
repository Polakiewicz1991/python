from dash import Input, Output, State, ctx, no_update
import plotly.graph_objs as go

from data_handler import parse_csv
from flatness_calculator import calculate_flatness
from plot3d import create_3d_scatter, create_3d_scatter_top

default_camera = dict(
    up=dict(x=0, y=0, z=1),
    center=dict(x=0, y=0, z=0),
    eye=dict(x=1.25, y=2, z=1.25)
)
default_camera2 = dict(
    up=dict(x=0, y=0, z=2),
    center=dict(x=0, y=0, z=0),
    eye=dict(x=1, y=0, z=3)
)

def register_callbacks(app):
    @app.callback(
        Output('three-d-plot-1', 'figure'),
        Output('three-d-plot-2', 'figure'),
        Output('three-d-plot-3', 'figure'),
        Output('flatness-output', 'children'),
        Input('upload-data', 'contents'),
        Input('reset-view-btn', 'n_clicks'),
        State('three-d-plot-1', 'figure'),
        State('three-d-plot-3', 'figure'),
        prevent_initial_call=True
    )
    def update_or_reset(contents, n_clicks, current_fig,current_fig2):
        triggered_id = ctx.triggered_id if hasattr(ctx, "triggered_id") else None

        if triggered_id == 'upload-data':
            if contents is None:
                empty_fig = go.Figure()
                empty_fig.update_layout(title='Wczytaj plik CSV, aby wyświetlić wykres')
                return empty_fig, empty_fig, empty_fig, ""
            try:
                df = parse_csv(contents)
            except Exception as e:
                empty_fig = go.Figure()
                empty_fig.update_layout(title=f"Błąd wczytywania pliku: {str(e)}")
                return empty_fig, empty_fig, empty_fig, ""

            flatness_value, coeffs, deviations = calculate_flatness(df)
            fig_new = create_3d_scatter(df, coeffs, deviations)
            fig_new2 = create_3d_scatter_top(df, coeffs, deviations)
            fig_new.update_layout(scene_camera=default_camera)
            fig_new2.update_layout(scene_camera=default_camera2)
            flatness_text = f"Płaskość powierzchni (metodą najmniejszych kwadratów): {flatness_value:.4f}"
            return fig_new, fig_new, fig_new2, flatness_text

        elif triggered_id == 'reset-view-btn' and current_fig is not None and current_fig2 is not None:
            current_fig['layout']['scene']['camera'] = default_camera
            current_fig2['layout']['scene']['camera'] = default_camera2
            return current_fig, current_fig, current_fig2, no_update

        empty_fig = go.Figure()
        empty_fig.update_layout(title='Wczytaj plik CSV, aby wyświetlić wykres')
        return empty_fig, empty_fig, empty_fig, ""