import dash
from dash.dependencies import Output, Input, State

import loader
from loader.load_cfg import conn_string


def register_callbacks(app):
    @app.callback(
        Output('curr_count_rows_etsp', 'children'),
        Output('count_rows_in_file_etsp', 'children'),
        Output('total_curr_rows_etsp', 'children'),
        Output('lbl_etsp_file_load', 'children'),
        Output('lbl_etsp_file_load', 'style'),
        Input('load_etsp_file_button', 'n_clicks'),
        State('etsp_link_input', 'value')
    )
    def click_load_etsp_btn(clicks, data_link_etsp):
        if clicks:
            if data_link_etsp:
                new_etsp_df = loader.get_etsp_data(data_link_etsp)
                rows_in_file = len(new_etsp_df)
                curr_count_rows = len(loader.load_data(table='etsp_data', connection_string=conn_string))
                total_count_rows = rows_in_file + curr_count_rows
                msg = 'Файл успешно обработан'
                msg_style = dict(color='green', fontWeight='bold')
                return curr_count_rows, rows_in_file, total_count_rows, msg, msg_style
            else:
                msg = 'При обработке файла возникли ошибки'
                msg_style = dict(color='red', fontWeight='bold')
                return dash.no_update, dash.no_update, dash.no_update, msg, msg_style
        return dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update

    @app.callback(
        Output('curr_count_rows_sue', 'children'),
        Output('count_rows_in_file_sue', 'children'),
        Output('total_curr_rows_sue', 'children'),
        Output('lbl_sue_file_load', 'children'),
        Output('lbl_sue_file_load', 'style'),
        Input('load_sue_file_button', 'n_clicks'),
        State('sue_link_input', 'value')
    )
    def click_load_sue_btn(clicks, data_link_sue):
        if clicks:
            if data_link_sue:
                sue_df = loader.get_sue_data(data_link_sue)
                rows_in_file = len(sue_df)
                curr_count_rows = len(loader.load_data(table='sue_data', connection_string=conn_string))
                total_count_rows = rows_in_file + curr_count_rows
                msg = 'Файл успешно обработан'
                msg_style = dict(color='green', fontWeight='bold')
                return curr_count_rows, rows_in_file, total_count_rows, msg, msg_style
            else:
                msg = 'При обработке файла возникли ошибки'
                msg_style = dict(color='red', fontWeight='bold')
                return dash.no_update, dash.no_update, dash.no_update, msg, msg_style
        return dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update

    @app.callback(
        Output('curr_count_rows_osp', 'children'),
        Output('count_rows_in_file_osp', 'children'),
        Output('total_curr_rows_osp', 'children'),
        Output('lbl_osp_file_load', 'children'),
        Output('lbl_osp_file_load', 'style'),
        Input('load_osp_file_button', 'n_clicks'),
        State('osp_link_input', 'value')
    )
    def click_load_osp_btn(clicks, data_link_osp):
        if clicks:
            if data_link_osp:
                osp_df = loader.get_osp_data(data_link_osp)
                rows_in_file = len(osp_df)
                curr_count_rows = len(loader.load_data(table='osp_data', connection_string=conn_string))
                total_count_rows = rows_in_file + curr_count_rows
                msg = 'Файл успешно обработан'
                msg_style = dict(color='green', fontWeight='bold')
                return curr_count_rows, rows_in_file, total_count_rows, msg, msg_style
            else:
                msg = 'При обработке файла возникли ошибки'
                msg_style = dict(color='red', fontWeight='bold')
                return dash.no_update, dash.no_update, dash.no_update, msg, msg_style
        return dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update
