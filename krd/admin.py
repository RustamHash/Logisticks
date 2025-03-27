from django.contrib import admin
from .models import Goods, Agent, Invoice, InvoiceBody


class GoodsAdmin(admin.ModelAdmin):
    list_display = ('id', 'marking_goods', 'item_name')
    search_fields = ('id', 'marking_goods', 'item_name')
    list_filter = ('id', 'marking_goods', 'item_name')

    class Meta:
        model = Goods
        fields = '__all__'


class AgentAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_name')
    search_fields = ('id', 'item_name')
    list_filter = ('id', 'item_name')

    class Meta:
        model = Agent
        fields = '__all__'


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'acs_number', 'from_id')
    search_fields = ('id', 'acs_number', 'from_id')
    list_filter = ('id', 'acs_number', 'from_id')

    class Meta:
        model = Invoice
        fields = '__all__'


class InvoiceBodyAdmin(admin.ModelAdmin):
    list_display = ('id', 'invoice_id')
    search_fields = ('id', 'invoice_id')
    list_filter = ('id', 'invoice_id')

    class Meta:
        model = InvoiceBody
        fields = '__all__'


admin.site.register(Goods, GoodsAdmin)
admin.site.register(Agent, AgentAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(InvoiceBody, InvoiceBodyAdmin)
