import os

import pandas as pd
from base_app.utils import data_to_dict, save_to_xml, upload_ftp
from base_app.utils import Logger
import inspect
import traceback

dic_log_return = {'Расход': 0, 'Приход': 0, 'Справочник товаров': 0, 'Справочник клиентов': 0, 'Сохранено': ''}
dic_columns = {0: 'Артикул', 1: 'Наименование', 2: 'Штрих-код упаковки', 3: 'Штрих-код блока', 4: 'Штрих-код короба',
               5: 'Вес нетто шт', 6: 'Вес брутто шт', 7: 'Штук в коробе',
               8: 'Штук в блоке', 9: 'Штук на палете', 10: 'Коробов на палете',
               11: 'Коробов в слое', 12: 'Длина шт в мм', 13: 'Ширина шт в мм', 14: 'Высота шт в мм',
               15: 'Обьем шт в м3', 16: 'Срок годности в днях', 17: 'Цена за шт'}

NUM_DATE = 0
NUM_TYPE = 1
NUM_ORDER = 2
NUM_ART_PRODUCT = 3
NUM_NAME_PRODUCT = 4
NUM_QTY_PRODUCT = 5
NUM_COMMENT = 6


def process_orders(**kwargs):
    func_name = inspect.currentframe().f_code.co_name
    try:
        for i in dic_log_return:
            dic_log_return[i] = 0
        kwargs['_df_order'], kwargs['_df_porder'] = __load_parse_file_order(kwargs.get('file_name'))
        if len(kwargs['_df_order']) > 0:
            __create_order(kwargs)
        if len(kwargs['_df_porder']) > 0:
            __create_porder(kwargs)
        return dic_log_return, True
    except Exception as e:
        Logger(
            module_name=__name__,
            func_name=func_name,
            message_error=str(e),
            traceback=traceback.format_exc()
        ).error()
        return {'error': str(e)}, False


def upload_product(**kwargs):
    func_name = inspect.currentframe().f_code.co_name
    try:
        for i in dic_log_return:
            dic_log_return[i] = 0
        _df_ka = __load_parse_file_order_goods(_file_name=kwargs.get('file_name'))
        kwargs['df'] = _df_ka
        __create_product(**kwargs)
        return dic_log_return, True
    except Exception as e:
        Logger(
            module_name=__name__,
            func_name=func_name,
            message_error=str(e),
            traceback=traceback.format_exc()
        ).error()
        return {'error': str(e)}, False


def __load_parse_file_order(_file_name):
    _df = pd.read_excel(_file_name, dtype=object)
    _df_order = _df[_df['ВидНакладной'] == 'Расход'].copy()
    _df_porder = _df[_df['ВидНакладной'] == 'Приход'].copy()
    return _df_order, _df_porder


def __load_parse_file_order_goods(_file_name):
    df = pd.read_excel(_file_name)
    df.rename(columns=lambda x: x.strip())
    df.reset_index(drop=True, inplace=True)
    return df


def __create_order(kwargs):
    _df = kwargs.get('_df_order')
    contract = kwargs.get('contract')
    df_order = pd.DataFrame()
    df_order['Itemid'] = _df[_df.columns[NUM_ART_PRODUCT]]
    df_order['Qty'] = _df[_df.columns[NUM_QTY_PRODUCT]]
    df_order['SalesId'] = _df[_df.columns[NUM_ORDER]]
    df_order['InventLocationId'] = contract.id_sklad
    df_order['ConsigneeAccount'] = contract.id_client
    df_order['DeliveryDate'] = _df[_df.columns[NUM_DATE]]
    df_order['ManDate'] = ''
    df_order['SalesUnit'] = 'шт'
    df_order['Delivery'] = contract.delivery_type
    df_order['Redelivery'] = 1
    df_order['OrderType'] = 1
    df_order['Comment'] = _df[_df.columns[NUM_COMMENT]]
    dic_order = data_to_dict(df_order)
    save_file_name = save_to_xml(dic_order, 'CustPicking', contract=contract)
    dic_log_return['Расход'] += len(dic_order)
    dic_log_return['Сохранено'] = f'В папку: {os.path.split(save_file_name)[0]}'
    if kwargs.get('dict_ftp_param'):
        upload_ftp(filenames=save_file_name, **kwargs.get('dict_ftp_param'))
        dic_log_return['Сохранено'] = (f'На ftp: {kwargs.get('dict_ftp_param').get('HOST')}\n'
                                       f' пользователь: {kwargs.get('dict_ftp_param').get('USERNAME')}\n'
                                       f' в папку {kwargs.get('dict_ftp_param').get('DIRECTORY')}')
        os.remove(save_file_name)


def __create_porder(kwargs):
    _df = kwargs.get('_df_porder')
    contract = kwargs.get('contract')
    df_porder = pd.DataFrame()
    df_porder['Itemid'] = _df[_df.columns[NUM_ART_PRODUCT]]
    df_porder['Qty'] = _df[_df.columns[NUM_QTY_PRODUCT]]
    df_porder['PurchId'] = _df[_df.columns[NUM_ORDER]]
    df_porder['VendAccount'] = contract.id_postav
    df_porder['DeliveryDate'] = _df[_df.columns[NUM_DATE]]
    df_porder['InventLocationId'] = contract.id_sklad
    df_porder['ProductionDate'] = '01.01.2023'
    df_porder['PurchUnit'] = 'шт'
    df_porder['PurchTTN'] = 1
    df_porder['Price'] = 0
    dic_order = data_to_dict(df_porder)
    save_file_name = save_to_xml(dic_order, 'VendReceipt', contract=contract)
    dic_log_return['Приход'] += len(dic_order)
    dic_log_return['Сохранено'] = f'В папку: {os.path.split(save_file_name)[0]}'
    if kwargs.get('dict_ftp_param'):
        upload_ftp(filenames=save_file_name, **kwargs.get('dict_ftp_param'))
        dic_log_return['Сохранено'] = (f'На ftp: {kwargs.get('dict_ftp_param').get('HOST')}\n'
                                       f' пользователь: {kwargs.get('dict_ftp_param').get('USERNAME')}\n'
                                       f' в папку {kwargs.get('dict_ftp_param').get('DIRECTORY')}')
        os.remove(save_file_name)


def __create_product(**kwargs):
    _df = kwargs.get('df')
    contract = kwargs.get('contract')
    df_product = pd.DataFrame()
    df_product['ItemId'] = _df[dic_columns[0]]
    df_product['ItemName'] = _df[dic_columns[1]]
    df_product['NetWeight'] = _df[dic_columns[6]]
    df_product['NetWeightBox'] = _df[dic_columns[6]]
    df_product['NetWeightPack'] = _df[dic_columns[6]]
    df_product['BruttoWeight'] = _df[dic_columns[6]]
    df_product['BruttoWeightBox'] = _df[dic_columns[6]]
    df_product['BruttoWeightPack'] = _df[dic_columns[6]]
    df_product['Quantity'] = _df[dic_columns[7]]
    df_product['standardShowBoxQuantity'] = 1
    df_product['UnitId'] = 'шт'
    df_product['Depth'] = _df[dic_columns[12]]
    df_product['Height'] = _df[dic_columns[14]]
    df_product['Width'] = _df[dic_columns[13]]
    df_product['BoxDepth'] = _df[dic_columns[12]]
    df_product['BoxHeight'] = _df[dic_columns[14]]
    df_product['BoxWidth'] = _df[dic_columns[13]]
    df_product['BlockDepth'] = _df[dic_columns[12]]
    df_product['BlockHeight'] = _df[dic_columns[14]]
    df_product['BlockWidth'] = _df[dic_columns[13]]
    df_product['StandardPalletQuantity'] = _df[dic_columns[9]]
    df_product['QtyPerLayer'] = 1
    df_product['Price'] = _df[dic_columns[17]]
    df_product['ShelfLife'] = _df[dic_columns[16]]
    df_product['EanBarcode'] = _df[dic_columns[2]]
    df_product['EanBarcodeBox'] = _df[dic_columns[2]]
    df_product['EanBarcodePack'] = _df[dic_columns[2]]
    df_product['Gs1Barcode'] = _df[dic_columns[2]]
    df_product['Gs1BarcodeBox'] = _df[dic_columns[2]]
    df_product['Gs1BarcodePack'] = _df[dic_columns[2]]
    dic_product = data_to_dict(df_product)
    save_file_name = save_to_xml(dic_product, 'InventTable', contract=contract)
    dic_log_return['Справочник товаров'] += len(dic_product)
    dic_log_return['Сохранено'] = f'В папку: {os.path.split(save_file_name)[0]}'
    if kwargs.get('dict_ftp_param'):
        upload_ftp(filenames=save_file_name, **kwargs.get('dict_ftp_param'))
        dic_log_return['Сохранено'] = (f'На ftp: {kwargs.get('dict_ftp_param').get('HOST')}\n'
                                       f' пользователь: {kwargs.get('dict_ftp_param').get('USERNAME')}\n'
                                       f' в папку {kwargs.get('dict_ftp_param').get('DIRECTORY')}')
        os.remove(save_file_name)
