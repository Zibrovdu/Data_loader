import dash_core_components as dcc
import dash_html_components as html


def serve_layout():
    tab_selected_style = dict(backgroundColor='#ebecf1',
                              fontWeight='bold')
    layout = html.Div([
        dcc.Location(id='url',
                     refresh=True),
        html.Div([
            html.H2('Обновление данных для дашбордов'),
            html.A([
                html.Img(src="assets/logo.png")
            ],
                href='#modal-1',
                className='js-modal-open link')
        ], className='banner'),
        html.Br(),
        html.Br(),
        html.Div([
            dcc.Tabs(
                id='',
                value='osp_dash',
                children=[
                    dcc.Tab(
                        value='osp_dash',
                        label='Дашборд ОСП',
                        children=[
                            html.Div([
                                html.Div([
                                    html.Div([
                                        html.Label(
                                            'Единый центр поддержки',
                                            className='label_etsp'
                                            # style=dict(
                                            #     fontSize='30px'
                                            # )
                                        ),
                                    ],
                                        className='div_label_etsp'
                                        # style=dict(
                                        #     padding='20px',
                                        #     width='370px',
                                        #     display='inline-block'
                                        # )
                                    ),
                                    html.Div([
                                        html.Img(
                                            src='assets/img/rtk.png',
                                            className='img_etsp'
                                            # style=dict(height='100px')
                                        )
                                    ],
                                        className='div_img_etsp'
                                        # style=dict(
                                        #     width='200px',
                                        #     float='right',
                                        #     display='inline-block')
                                    ),
                                    html.Div([
                                        html.Div([
                                            dcc.Input(
                                                id='etsp_link_input',
                                                placeholder='Вставьте ссылку на файл с данными ЕЦП',
                                                className='input_etsp_link'
                                            )
                                        ],
                                            className='div_lbl_btn'
                                        ),
                                        html.Div([
                                            html.Button(
                                                'Загрузить',
                                                id='load_etsp_file_button',
                                                className='button_load_etsp'
                                            )
                                        ],
                                            className='div_lbl_btn'
                                        )
                                    ])
                                ],
                                    className='div_etsp'
                                    # style=dict(
                                    #     border='1px solid darkblue',
                                    #     borderRadius='10px',
                                    #     width='auto',
                                    #     height='400px',
                                    #     margin='25px 15px'
                                    # )
                                )
                            ])

                        ],
                        selected_style=tab_selected_style
                    ),
                    dcc.Tab(
                        value='oitscb',
                        label='Дашборд ОИТС ЦБ',
                        children=[],
                        selected_style=tab_selected_style
                    )
                ],
            )
        ]),

        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        'История изменений'
                    ], className='modal__dialog-header-content'),
                    html.Div([
                        html.Button([
                            html.Span('x')
                        ], className='js-modal-close modal__dialog-header-close-btn')
                    ], className='modal__dialog-header-close')
                ], className='modal__dialog-header'),
                html.Div([
                    html.Br(),
                    html.Div([
                        dcc.Textarea(value="", readOnly=True, className='frame-history')
                    ]),
                    html.Br(),
                ], className='modal__dialog-body'),
                html.Div([
                    html.Button('Close', className='js-modal-close modal__dialog-footer-close-btn')
                ], className='modal__dialog-footer')
            ], className='modal__dialog')
        ], id='modal-1', className='modal_history modal--l'),
        html.Script(src='assets/js/main.js'),

    ], className='bg_color')
    return layout
