from django.contrib import admin
from ut.application.models import ApplicationPorderItems, ApplicationOrderItems, Application


class ApplicationPorderAdmin(admin.ModelAdmin):
    list_display = ('number', 'date', 'filial', 'contract')
    search_fields = ('number', )
    list_filter = ('number', 'date', 'filial', 'contract')
    ordering = ('date', 'filial', 'contract', 'number')

    class Meta:
        model = Application
        fields = '__all__'


admin.site.register(Application, ApplicationPorderAdmin)