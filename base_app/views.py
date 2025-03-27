from django.shortcuts import render
from django.contrib import messages

from .models import Filial, Menu, SubMenu, Contracts
from base_app.forms import ContractsForm, FileUploadForm, ReportFiltersDateForm, PeriodForm
import logging

logger = logging.getLogger(__name__)


def home(request, **kwargs):
    logger.error('Start home')
    kwargs['filials'] = Filial.objects.filter(as_active=True)
    kwargs['filial_active'] = None
    return render(request, 'base_app/filials.html', kwargs)


def filial_home(request, **kwargs):
    logger.error('Start filial_home')
    kwargs['filial'] = Filial.objects.filter(as_active=True, slug=kwargs['filial_selected'])
    kwargs['menus'] = Menu.objects.filter(as_active=True, filial__slug=kwargs['filial_selected'])
    return render(request, 'base_app/home.html', context=kwargs)


def operations(request, **kwargs):
    logger.error('Start operations')
    kwargs['menus'] = Menu.objects.filter(as_active=True, filial__slug=kwargs['filial_selected'])
    kwargs['submenus'] = SubMenu.objects.filter(menu__slug=kwargs['menu_selected'])
    return render(request, 'base_app/home.html', context=kwargs)


def process_orders(request, **kwargs):
    logger.error('Start process_orders')
    kwargs['menus'] = Menu.objects.filter(as_active=True, filial__slug=kwargs['filial_selected'])
    kwargs['submenus'] = SubMenu.objects.filter(menu__slug=kwargs['menu_selected'])
    kwargs['submenu'] = SubMenu.objects.get(slug=kwargs['submenu_selected'])
    kwargs['contracts'] = kwargs['submenu'].contract.filter(as_active=True, filial__slug=kwargs['filial_selected'])
    kwargs['form_contract'] = ContractsForm(submenu=kwargs['contracts'])
    kwargs['form_file_upload'] = FileUploadForm()
    if request.method == 'POST':
        contract = Contracts.objects.get(pk=request.POST['contract'])
        print(contract)
        print(request.POST)
        start_date = request.POST['start_date']
        print(start_date)
        print(type(start_date))
        if request.FILES.get('file'):
            print(request.FILES['file'])
    return render(request, 'base_app/operations.html', context=kwargs)


def operation(request, **kwargs):
    logger.error('Start operation')
    kwargs['menus'] = Menu.objects.filter(as_active=True, filial__slug=kwargs['filial_selected'])
    kwargs['submenus'] = SubMenu.objects.filter(menu__slug=kwargs['menu_selected'])
    kwargs['submenu'] = SubMenu.objects.get(slug=kwargs['submenu_selected'])
    kwargs['contracts'] = kwargs['submenu'].contract.filter(as_active=True, filial__slug=kwargs['filial_selected'])
    kwargs['form_date'] = PeriodForm()
    kwargs['form_contract'] = ContractsForm(submenu=kwargs['contracts'])
    kwargs['form_file_upload'] = FileUploadForm()
    # kwargs['form'] = ContractsForm(filial_slug=kwargs['filial_selected'])
    # if request.method == 'POST':
    #     print(request.POST)
    #     if request.FILES.get('file'):
    #         print(request.FILES['file'])
    return render(request, 'base_app/operations.html', context=kwargs)


def error_reverse_url(request, **kwargs):
    logger.error('Start error_reverse_url')
    logger.error(kwargs)
    logger.error(f'Не указан путь для: {kwargs["submenu_selected"]}')
    kwargs['menus'] = Menu.objects.filter(as_active=True, filial__slug=kwargs['filial_selected'])
    kwargs['submenus'] = SubMenu.objects.filter(menu__slug=kwargs['menu_selected'])
    messages.error(request, f'Не указан путь для {kwargs["submenu_selected"]}')
    return render(request, 'base_app/home.html', context=kwargs)


def billing_tls(request, **kwargs):
    logger.error('Start billing_tls')
    kwargs['menus'] = Menu.objects.filter(as_active=True, filial__slug=kwargs['filial_selected'])
    kwargs['submenus'] = SubMenu.objects.filter(menu__slug=kwargs['menu_selected'])
    print(kwargs)
    return render(request, 'base_app/reports.html', context=kwargs)
