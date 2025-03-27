from django.urls import path

from base_app.views import (error_reverse_url, home, filial_home, operations, operation, process_orders)
from base_app.models import Filial, Menu, SubMenu

dict_operations = {
    'process_orders': process_orders,
    'upload_product': operation,
    'upload_clients': operation,
}

app_name = "base_app"

urlpatterns = [
    path('', home, name='home'),
]


def create_urls(app_name_new):
    _l = []
    filial_active = Filial.objects.get(slug=app_name_new)
    menus = filial_active.menus.filter(as_active=True)
    _l.append(path('', filial_home, kwargs={
        'filial_selected': app_name_new,
        'filial_active': filial_active,
        'menu_selected': None,
        'submenu_selected': None,
    },
                   name=f'{app_name_new}_home'), )
    for menu in menus:
        _url = path(menu.slug, operations, name=f'{menu.slug}',
                    kwargs={
                        'filial_active': filial_active,
                        'filial_selected': app_name_new,
                        'menu_selected': menu.slug,
                        'submenu_selected': None,
                    })
        _l.append(_url)
        submenus = SubMenu.objects.filter(menu__slug=menu.slug)
        for submenu in submenus:
            _url = path(f"{menu.slug}/{submenu.slug}", dict_operations.get(submenu.slug, error_reverse_url),
                        name=f'{submenu.slug}',
                        kwargs={
                            'filial_active': filial_active,
                            'filial_selected': app_name_new,
                            'menu_selected': menu.slug,
                            'submenu_selected': submenu.slug,
                        }
                        )
            _l.append(_url)
    return _l
