import configparser

from sqlalchemy import create_engine

cfg_parser = configparser.ConfigParser()
cfg_parser.read(r'assets/settings.rkz')

db_username = cfg_parser['connect']['username']
db_password = cfg_parser['connect']['password']
db_name = cfg_parser['connect']['db']
db_host = cfg_parser['connect']['host']
db_port = cfg_parser['connect']['port']
db_dialect = cfg_parser['connect']['dialect']


conn_string = create_engine(f'{db_dialect}://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}')
