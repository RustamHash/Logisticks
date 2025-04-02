import inspect
import traceback

from base_app.contract_models import standart
from base_app.utils import Logger

dict_func = dict(process_orders=standart.process_orders, upload_product=standart.upload_product)
__dict_ftp_param = {'HOST': 'ftp.rnd.gk21.ru', 'USERNAME': 'ynigra', 'PASSWORD': 'EaDGruteS25',
                    'DIRECTORY': 'rnd/in'}


def start(**kwargs):
    func_name = inspect.currentframe().f_code.co_name
    try:
        if kwargs.get('ftp'):
            kwargs['dict_ftp_param'] = __dict_ftp_param
        res, error_valid = dict_func.get(kwargs['submenu_selected'])(**kwargs)
        print(f'res: {res} error_valid: {error_valid}')
        if error_valid:
            Logger(module_name=__name__, func_name=func_name).info()
            return res
        else:
            result = {'error': f'Ошибка обработки\n{res}'}
            return result

    except Exception as e:
        Logger(
            module_name=__name__,
            func_name=func_name,
            message_error=str(e),
            traceback=traceback.format_exc()
        ).error()
        result = {'error': traceback.format_exc()}
        return result
