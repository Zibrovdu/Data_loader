import dash
from dash.dependencies import Output, Input

import loader
from loader.load_cfg import conn_string


def register_callbacks(app):
    @app.callback(
        Output('etsp_info', 'children'),
        Output('etsp_info', 'style'),
        Output('curr_count_rows', 'children'),
        Output('rows_in_file', 'children'),
        Output('total_count_rows', 'children'),
        Input('load_etsp_btn', 'n_clicks'),
        Input('etsp_input', 'value')
    )
    def click_load_etsp_btn(n_clicks, data_link_etsp):
        ...
