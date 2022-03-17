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
                                            'Единый центр поддержки (Ростелеком)',
                                            className='label_etsp'
                                        ),
                                    ],
                                        className='div_label_etsp'
                                    ),
                                    html.Div([
                                        html.Img(
                                            src='assets/img/rtk.png',
                                            className='img_etsp'
                                        )
                                    ],
                                        className='div_img_etsp'
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
                                    ]),
                                    html.Div([
                                        dcc.Loading(id='load_etsp',
                                                    children=[
                                                        html.Div([
                                                            html.Label(
                                                                id='lbl_etsp_file_load'
                                                            )
                                                        ],
                                                            className='div_lbl_btn'
                                                        ),
                                                        html.Table([
                                                            html.Th([
                                                                html.Label('Параметр')
                                                            ]),
                                                            html.Th([
                                                                html.Label('Значение')
                                                            ]),
                                                            html.Tr([
                                                                html.Td([
                                                                    html.Label('Записей в БД на текущий момент')
                                                                ]),
                                                                html.Td([
                                                                    html.Label(id='curr_count_rows_etsp')
                                                                ]),
                                                            ],
                                                            ),
                                                            html.Tr([
                                                                html.Td([
                                                                    html.Label('Записей в загруженном файле')
                                                                ]),
                                                                html.Td([
                                                                    html.Label(id='count_rows_in_file_etsp')
                                                                ]),
                                                            ],
                                                            ),
                                                            html.Tr([
                                                                html.Td([
                                                                    html.Label(
                                                                        'Итого записей'
                                                                    )
                                                                ]),
                                                                html.Td([
                                                                    html.Label(
                                                                        id='total_curr_rows_etsp'
                                                                    )
                                                                ]),
                                                            ],
                                                            ),
                                                        ]), ])
                                    ],
                                        className='div_table'
                                    )
                                ],
                                    className='div_etsp'
                                ),
                                html.Div([
                                    html.Div([
                                        html.Label(
                                            'Система управления и эксплуатации (СУЭ)',
                                            className='label_etsp'
                                        ),
                                    ],
                                        className='div_label_etsp'
                                    ),
                                    html.Div([
                                        html.Img(
                                            src='assets/img/sue.png',
                                            className='img_sue'
                                        )
                                    ],
                                        className='div_img_etsp'
                                    ),
                                    html.Div([
                                        html.Div([
                                            dcc.Input(
                                                id='sue_link_input',
                                                placeholder='Вставьте ссылку на файл с данными СУЭ',
                                                className='input_etsp_link'
                                            )
                                        ],
                                            className='div_lbl_btn'
                                        ),
                                        html.Div([
                                            html.Button(
                                                'Загрузить',
                                                id='load_sue_file_button',
                                                className='button_load_sue'
                                            )
                                        ],
                                            className='div_lbl_btn'
                                        )
                                    ]),

                                    html.Div([
                                        dcc.Loading(id='load_sue',
                                                    children=[
                                                        html.Div([
                                                            html.Label(
                                                                id='lbl_sue_file_load'
                                                            )
                                                        ],
                                                            className='div_lbl_btn'
                                                        ),
                                                        html.Table([
                                                            html.Th([
                                                                html.Label('Параметр')
                                                            ]),
                                                            html.Th([
                                                                html.Label('Значение')
                                                            ]),
                                                            html.Tr([
                                                                html.Td([
                                                                    html.Label('Записей в БД на текущий момент')
                                                                ]),
                                                                html.Td([
                                                                    html.Label(id='curr_count_rows_sue')
                                                                ]),
                                                            ],
                                                            ),
                                                            html.Tr([
                                                                html.Td([
                                                                    html.Label('Записей в загруженном файле')
                                                                ]),
                                                                html.Td([
                                                                    html.Label(id='count_rows_in_file_sue')
                                                                ]),
                                                            ],
                                                            ),
                                                            html.Tr([
                                                                html.Td([
                                                                    html.Label('Итого записей')
                                                                ]),
                                                                html.Td([
                                                                    html.Label(
                                                                        id='total_curr_rows_sue'
                                                                    )
                                                                ]),
                                                            ],
                                                            ),
                                                        ]), ])
                                    ],
                                        className='div_table'
                                    )

                                ],
                                    className='div_sue'
                                ),
                                html.Div([
                                    html.Div([
                                        html.Label(
                                            'Отдел сопровождения пользователей (ОСП)',
                                            className='label_etsp'
                                        ),
                                    ],
                                        className='div_label_etsp'
                                    ),
                                    html.Div([
                                        html.Img(
                                            src='assets/img/osp.png',
                                            className='img_sue'
                                        )
                                    ],
                                        className='div_img_etsp'
                                    ),
                                    html.Div([
                                        html.Div([
                                            dcc.Input(
                                                id='osp_link_input',
                                                placeholder='Вставьте ссылку на файл с данными СУЭ',
                                                className='input_etsp_link'
                                            )
                                        ],
                                            className='div_lbl_btn'
                                        ),
                                        html.Div([
                                            html.Button(
                                                'Загрузить',
                                                id='load_osp_file_button',
                                                className='button_load_sue'
                                            )
                                        ],
                                            className='div_lbl_btn'
                                        )
                                    ]),
                                    html.Div([
                                        dcc.Loading(id='load_osp', children=[
                                            html.Div([
                                                html.Label(
                                                    id='lbl_osp_file_load'
                                                )
                                            ],
                                                className='div_lbl_btn'
                                            ),
                                            html.Table([
                                                html.Th([
                                                    html.Label('Параметр')
                                                ]),
                                                html.Th([
                                                    html.Label('Значение')
                                                ]),
                                                html.Tr([
                                                    html.Td([
                                                        html.Label('Записей в БД на текущий момент')
                                                    ]),
                                                    html.Td([
                                                        html.Label(id='curr_count_rows_osp')
                                                    ]),
                                                ],
                                                ),
                                                html.Tr([
                                                    html.Td([
                                                        html.Label('Записей в загруженном файле')
                                                    ]),
                                                    html.Td([
                                                        html.Label(id='count_rows_in_file_osp')
                                                    ]),
                                                ],
                                                ),
                                                html.Tr([
                                                    html.Td([
                                                        html.Label(
                                                            'Итого записей'
                                                        )
                                                    ]),
                                                    html.Td([
                                                        html.Label(
                                                            id='total_curr_rows_osp'
                                                        )
                                                    ]),
                                                ],
                                                ),
                                            ]), ])
                                    ],
                                        className='div_table'
                                    )

                                ],
                                    className='div_osp'
                                ),
                                html.Div([
                                    html.Div([
                                        html.Button('Обработать все файлы', id='all_files', className='btn_all_files')
                                    ])
                                ],
                                         className='div_osp'
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
