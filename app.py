import dash

from loader.callbacks import register_callbacks
from loader.layouts import serve_layout

app = dash.Dash(__name__,
                suppress_callback_exceptions=True,
                title='Обновление данных для дашбордов')
server = app.server

app.layout = serve_layout
register_callbacks(app)

if __name__ == '__main__':
    app.run_server()
