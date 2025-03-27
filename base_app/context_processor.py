from django.urls import resolve
from base_app.models import Filial, Menu
from base_app.urls import urlpatterns, create_urls

def get_filials(request):
    res = Filial.objects.filter(as_active=True)
    # print(f'urlpatterns: {urlpatterns}')
    # x = create_urls('krd')
    # print(x)
    if res:
        return {'get_filials': res}
    else:
        return {'get_filials': None}


def get_menus(request):
    filial_selected = request.resolver_match.kwargs.get('filial_slug', None)
    res = Menu.objects.filter(as_active=True, filial__slug=filial_selected)
    if res:
        return {'get_menus': res}
    else:
        return {'get_menus': None}



#
# def get_app_name(request):
#     app_name = request.resolver_match.kwargs
#     res = Filial.objects.filter(slug=app_name)
#     if res:
#         return {'get_filial': res}
#     else:
#         return {'get_filial': None}
#
#
# def get_url_name(request):
#     url_name = resolve(request.path_info).url_name
#     return {
#         'url_name': url_name
#     }
#
#
# def get_contract_list(request):
#     app_name = resolve(request.path_info).view_name
#     res = Contracts.objects.filter(menu__filial__slug=app_name.split(':')[0])
#     if res:
#         return {'contracts_list': res}
#     else:
#         return {'contracts_list': 'None'}
