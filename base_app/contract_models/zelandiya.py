import inspect
import traceback

import pandas as pd
from base_app.contract_models import standart, reports_standart
from pg.models import PG

dic_columns = {0: 'Артикул', 1: 'Номенклатура', 2: 'штрих-код шт', 3: 'штрих-код блок', 4: 'штрих-код короб',
               5: 'Вес нетто, шт', 6: 'Вес брутто, шт', 7: 'Количество шт. в коробе', 8: 'Количество шт. в блоке',
               9: 'Количество шт. в паллете', 10: 'Количество коробов на паллете', 11: 'Количество  коробов в слое',
               12: 'Длина шт. в мм', 13: 'Ширина шт. в мм', 14: 'Высота шт. в мм', 15: 'Обьем шт. в м3',
               16: 'Срок годности в днях', 17: 'Цена за шт. для расчетов убытков'}

dict_func_operation = dict(process_orders=standart.process_orders, upload_product=standart.upload_product)
__dict_ftp_param = {'HOST': 'ftp.rnd.gk21.ru', 'USERNAME': 'ynigra', 'PASSWORD': 'EaDGruteS25',
                    'DIRECTORY': 'rnd/in'}


def start(**kwargs):
    try:
        if kwargs['submenu_selected'] in dict_func_operation.keys():
            __get_df_goods(kwargs['file_name'])
            kwargs['file_name'] = 'products.xlsx'
            if kwargs.get('ftp'):
                kwargs['dict_ftp_param'] = __dict_ftp_param
            res, error_valid = dict_func.get(kwargs['submenu_selected'])(**kwargs)
            if error_valid:
                return res
            else:
                result = {'error': f'Ошибка обработки\n{res}'}
                return result
        elif kwargs['submenu_selected'] in dict_func.keys():
            dict_func.get(kwargs['submenu_selected'])(**kwargs)

    except Exception as e:
        result = {'error': traceback.format_exc()}
        return result


def __get_df_goods(_file_name):
    _df_new = pd.read_excel(_file_name, dtype='object')
    df = _df_new.dropna(subset=[_df_new.columns[1]])
    df.columns = df.iloc[3]
    df.rename(columns=lambda x: x.strip())
    df.drop(df.index[:4], inplace=True)
    df.reset_index(drop=True, inplace=True)
    df.rename(columns=dict(zip(list(dic_columns.values()), list(standart.dic_columns.values()))), inplace=True)
    df.to_excel(f'products.xlsx', index=False)


def billing_tls(**kwargs):
    func_name = inspect.currentframe().f_code.co_name
    reports_standart.billing_tls(**kwargs)
    # contract = kwargs['contract']
    # url_pg = contract.filial.url_pg
    # prog_id = contract.filial.prog_id
    # id_agent = contract.id_agent
    # start_date = kwargs['start_date']
    # end_date = kwargs['end_date']
    # filter_query = {'agent_id': id_agent, 'program_id': prog_id, 'delivery': True}

    # df = PG().get_invoice(pg_url=url_pg, start_date=start_date, end_date=end_date, filter_query=filter_query)
    # print(df.to_markdown())
    # df.to_excel('invoices.xlsx', index=False)


dict_func = dict(billing_tls=billing_tls)
