from django.shortcuts import render, resolve_url, redirect, reverse
from Logistics.settings import FILIAL_ACTIVE

context = {}


def filial_home(request, filial_slug=None):
    context['filial_selected'] = filial_slug
    return render(request, f'base_app/filial.html', context=context)
