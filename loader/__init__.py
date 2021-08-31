import pandas as pd
import nltk

from loader.load_cfg import conn_string


def get_unit_name(df, connection_string):
    empl_df = pd.read_sql("""select curr_name, curr_unit from employees where status = 'Работает'""",
                          con=connection_string)
    empl_df.columns = ['name', 'unit']

    df['new_name'] = ''
    for num in df.index:
        for name in empl_df.name:
            d = nltk.edit_distance(name.lower(), df.user.loc[num].lower())
            diff = d / len(name)
            if diff < 0.1:
                df['new_name'].loc[num] = name

    df['is_name_correct'] = df.user == df.new_name
    mask = df[df.is_name_correct == False].index
    df.loc[mask, 'new_name'] = df.loc[mask, 'user']

    check = len(df) == len(df[df.is_name_correct == True]) + len(df[df.is_name_correct == False])
    df.drop(['user', 'is_name_correct'], axis=1, inplace=True)

    df = df.merge(empl_df, how='left', left_on=['new_name'], right_on=['name'])
    df.drop(['name'], axis=1, inplace=True)
    df['unit'].fillna('Отдел не определен', inplace=True)

    if check:
        return df
    else:
        pd.DataFrame()


def load_etsp_data(connection_string):
    etsp_df = pd.read_sql('''select * from etsp_data''', con=connection_string)
    etsp_df.timedelta = pd.to_timedelta(etsp_df.timedelta)
    return etsp_df


def count_rows(df):
    return "Записей в БД на текущий момент: " + str(len(df))


def count_rows_load(df):
    return "Записей в загруженном файле: " + str(len(df))


def total_count_rows(df, new_df):
    return f'Итого записей: {str(len(df) + len(new_df))}'


def get_etsp_data(data_link_etsp):
    new_etsp_df = pd.read_excel(f'{data_link_etsp}/download', usecols='A,E,F,H,K')
    new_etsp_df.columns = ['num', 'user', 'reg_date', 'solved_date', 'descr']

    new_etsp_df['reg_date'] = pd.to_datetime(new_etsp_df['reg_date'], format='%d.%m.%y %H:%M')
    new_etsp_df['solved_date'] = pd.to_datetime(new_etsp_df['solved_date'], format='%d.%m.%y %H:%M')

    mask = new_etsp_df[new_etsp_df.solved_date.notna()].index
    new_etsp_df.loc[mask, 'timedelta'] = pd.to_timedelta(
        new_etsp_df[new_etsp_df.solved_date.notna()].solved_date - new_etsp_df[
            new_etsp_df.solved_date.notna()].reg_date)

    new_etsp_df = get_unit_name(new_etsp_df, connection_string=conn_string)

    new_etsp_df['start_date'] = new_etsp_df['reg_date'].dt.date.apply(lambda x: str(x))
    new_etsp_df['finish_date'] = new_etsp_df['solved_date'].dt.date.apply(lambda x: str(x))

    new_etsp_df['month_open'] = new_etsp_df['reg_date'].dt.month
    mask = new_etsp_df[new_etsp_df.solved_date.notna()].index
    new_etsp_df.loc[mask, 'month_solved'] = new_etsp_df[new_etsp_df.solved_date.notna()].solved_date.dt.month

    new_etsp_df['week_open'] = new_etsp_df['reg_date'].dt.isocalendar()['week']
    mask = new_etsp_df[new_etsp_df.solved_date.notna()].index
    new_etsp_df.loc[mask, 'week_solved'] = new_etsp_df[new_etsp_df.solved_date.notna()].solved_date.dt.isocalendar()[
        'week']

    new_etsp_df['count_task'] = 1

    new_etsp_df = new_etsp_df[['num', 'new_name', 'reg_date', 'solved_date', 'descr', 'timedelta', 'unit', 'start_date',
                               'finish_date', 'month_open', 'month_solved', 'week_open', 'week_solved', 'count_task']]
    new_etsp_df.columns = ['num', 'user', 'reg_date', 'solved_date', 'descr', 'timedelta', 'unit', 'start_date',
                           'finish_date', 'month_open', 'month_solved', 'week_open', 'week_solved', 'count_task']

    return new_etsp_df

# def get_osp_data(data_link_osp):
#     osp_df = pd.read_excel(f'{data_link_osp}/download', usecols='B,D,S,AG,AH')
#     osp_df.columns = ['reg_date', 'user', 'descr', 'plan_date', 'solved_date']
#
#     osp_df['timedelta'] = osp_df['solved_date'] - osp_df['reg_date']
#
#     osp_df = get_unit_name(osp_df)
#
#     osp_df['start_date'] = osp_df['reg_date'].dt.date.apply(lambda x: str(x))
#     osp_df['finish_date'] = osp_df['solved_date'].dt.date.apply(lambda x: str(x))
#
#     osp_df['month_open'] = osp_df['reg_date'].dt.month
#     osp_df['month_solved'] = osp_df['solved_date'].dt.month
#
#     osp_df['week_open'] = osp_df['reg_date'].dt.isocalendar()['week']
#     osp_df['week_solved'] = osp_df['solved_date'].dt.isocalendar()['week']
#
#     osp_df['count_task'] = 1
#
#     osp_df = osp_df[['reg_date', 'new_name', 'descr', 'plan_date', 'solved_date', 'timedelta', 'unit', 'start_date',
#                      'finish_date', 'month_open', 'month_solved', 'week_open', 'week_solved', 'count_task']]
#     osp_df.columns = ['reg_date', 'user', 'descr', 'plan_date', 'solved_date', 'timedelta', 'unit', 'start_date',
#                       'finish_date', 'month_open', 'month_solved', 'week_open', 'week_solved', 'count_task']
#
#     return osp_df
