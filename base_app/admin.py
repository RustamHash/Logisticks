from django.contrib import admin
from django.forms import TextInput
from django.db import models

from .models import Filial, Menu, SubMenu, Contracts


class FilialAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name']

    class Meta:
        model = Filial
        fields = '__all__'


class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name']

    class Meta:
        model = Menu
        fields = '__all__'


class SubMenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'menu')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['menu', 'name']

    class Meta:
        model = SubMenu
        fields = '__all__'


class ContractsAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'filial')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['filial', 'name']
    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'size': '20'})},
        models.CharField: {'widget': TextInput(attrs={'size': '100'})},
    }

    class Meta:
        model = Contracts
        fields = '__all__'


admin.site.register(Filial, FilialAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(SubMenu, SubMenuAdmin)
admin.site.register(Contracts, ContractsAdmin)
