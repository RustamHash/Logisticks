import inspect
import traceback

from django.shortcuts import render
from django.contrib import messages

from base_app.models import Filial, Menu, SubMenu, Contracts

from base_app.forms import ContractsForm, FileUploadForm, ReportFiltersDateForm, PeriodForm
from base_app.utils import Logger

from base_app.contract_models.krd import kzvs
from base_app.contract_models import zelandiya



dict_contract_func = {
    'kzvs': kzvs,
    'zelandiya_krd': zelandiya,
}


def home(request, **kwargs):
    # from ut.models import Agent
    # Agent.objects.all().delete()
    func_name = inspect.currentframe().f_code.co_name
    try:
        kwargs['filials'] = Filial.objects.filter(as_active=True)
        kwargs['filial_active'] = None
        Logger(module_name=__name__, func_name=func_name).info()
        return render(request, 'base_app/filials.html', kwargs)
    except Exception as e:
        Logger(
            module_name=__name__,
            func_name=func_name,
            message_error=str(e),
            traceback=traceback.format_exc()
        ).error()


def filial_home(request, **kwargs):
    func_name = inspect.currentframe().f_code.co_name
    try:
        kwargs['filial'] = Filial.objects.filter(as_active=True, slug=kwargs['filial_selected'])
        kwargs['menus'] = Menu.objects.filter(as_active=True, filial__slug=kwargs['filial_selected'])
        Logger(module_name=__name__, func_name=func_name).info()
        return render(request, 'base_app/home.html', context=kwargs)
    except Exception as e:
        Logger(
            module_name=__name__,
            func_name=func_name,
            message_error=str(e),
            traceback=traceback.format_exc()
        ).error()


def operations(request, **kwargs):
    func_name = inspect.currentframe().f_code.co_name
    try:
        kwargs['menus'] = Menu.objects.filter(as_active=True, filial__slug=kwargs['filial_selected'])
        kwargs['submenus'] = SubMenu.objects.filter(menu__slug=kwargs['menu_selected'])
        return render(request, 'base_app/home.html', context=kwargs)
    except Exception as e:
        Logger(
            module_name=__name__,
            func_name=func_name,
            message_error=str(e),
            traceback=traceback.format_exc()
        ).error()


def operation(request, **kwargs):
    func_name = inspect.currentframe().f_code.co_name
    try:
        kwargs['menus'] = Menu.objects.filter(as_active=True, filial__slug=kwargs['filial_selected'])
        kwargs['submenus'] = SubMenu.objects.filter(menu__slug=kwargs['menu_selected'])
        kwargs['submenu'] = SubMenu.objects.get(slug=kwargs['submenu_selected'])
        kwargs['contracts'] = kwargs['submenu'].contract.filter(as_active=True,
                                                                filial__slug=kwargs['filial_selected']).order_by('name')
        kwargs['form_contract'] = ContractsForm(submenu=kwargs['contracts'])
        kwargs['form_file_upload'] = FileUploadForm()
        if request.method == 'POST':
            contract = Contracts.objects.get(pk=request.POST['contract'])
            contract_func = dict_contract_func.get(contract.slug, None)
            if not contract_func:
                messages.error(request, f'Не создана обработка для: {contract.slug} {contract.name}')
                return render(request, 'base_app/operations.html', context=kwargs)
            file = request.FILES['file']
            if request.POST.get('ftp') and contract.ftp_bool:
                ftp = True
            else:
                ftp = False
            data = {
                'file_name': file,
                'contract': contract,
                'submenu_selected': kwargs['submenu_selected'],
                'ftp': ftp
            }
            kwargs['result'] = contract_func.start(**data)
        Logger(module_name=__name__, func_name=func_name).info()
        return render(request, 'base_app/operations.html', context=kwargs)
    except Exception as e:
        Logger(
            module_name=__name__,
            func_name=func_name,
            message_error=str(e),
            traceback=traceback.format_exc()
        ).error()
        return render(request, 'base_app/home.html', context=kwargs)


def report(request, **kwargs):
    print(kwargs)
    func_name = inspect.currentframe().f_code.co_name
    try:
        kwargs['menus'] = Menu.objects.filter(as_active=True, filial__slug=kwargs['filial_selected'])
        kwargs['submenus'] = SubMenu.objects.filter(menu__slug=kwargs['menu_selected'])
        kwargs['submenu'] = SubMenu.objects.get(slug=kwargs['submenu_selected'])
        kwargs['contracts'] = kwargs['submenu'].contract.filter(as_active=True,
                                                                filial__slug=kwargs['filial_selected']).order_by('name')
        kwargs['form_contract'] = ContractsForm(submenu=kwargs['contracts'])
        kwargs['form_file_upload'] = PeriodForm()
        if request.method == 'POST':
            print(request.POST)
            contract = Contracts.objects.get(pk=request.POST['contract'])
            contract_func = dict_contract_func.get(contract.slug, None)
            if not contract_func:
                messages.error(request, f'Не создана обработка для: {contract.slug} {contract.name}')
                return render(request, 'base_app/reports.html', context=kwargs)
            data = {
                'contract': contract,
                'submenu_selected': kwargs['submenu_selected'],
                'start_date': request.POST['start_date'],
                'end_date': request.POST['end_date']
            }
            kwargs['result'] = contract_func.start(**data)
        Logger(module_name=__name__, func_name=func_name).info()
        return render(request, 'base_app/reports.html', context=kwargs)
    except Exception as e:
        Logger(
            module_name=__name__,
            func_name=func_name,
            message_error=str(e),
            traceback=traceback.format_exc()
        ).error()
        return render(request, 'base_app/home.html', context=kwargs)


def error_reverse_url(request, **kwargs):
    func_name = inspect.currentframe().f_code.co_name
    try:
        kwargs['menus'] = Menu.objects.filter(as_active=True, filial__slug=kwargs['filial_selected'])
        kwargs['submenus'] = SubMenu.objects.filter(menu__slug=kwargs['menu_selected'])
        messages.error(request, f'Не указан путь для {kwargs["submenu_selected"]}')
        Logger(module_name=__name__, func_name=func_name).info()
        return render(request, 'base_app/home.html', context=kwargs)
    except Exception as e:
        Logger(
            module_name=__name__,
            func_name=func_name,
            message_error=str(e),
            traceback=traceback.format_exc()
        ).error()


def billing_tls(request, **kwargs):
    func_name = inspect.currentframe().f_code.co_name
    try:
        kwargs['menus'] = Menu.objects.filter(as_active=True, filial__slug=kwargs['filial_selected'])
        kwargs['submenus'] = SubMenu.objects.filter(menu__slug=kwargs['menu_selected'])
        Logger(module_name=__name__, func_name=func_name).info()
        return render(request, 'base_app/reports.html', context=kwargs)
    except Exception as e:
        Logger(
            module_name=__name__,
            func_name=func_name,
            message_error=str(e),
            traceback=traceback.format_exc()
        ).error()
