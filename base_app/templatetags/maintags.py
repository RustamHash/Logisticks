from django import template
from django.urls import reverse_lazy

register = template.Library()


@register.simple_tag(takes_context=True)
def create_url_name(context, data):
    data = f"{context['filial_selected']}:{data}"
    return reverse_lazy(data)
