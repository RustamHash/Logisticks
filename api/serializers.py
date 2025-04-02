from django.db.models import Sum
from rest_framework import serializers
from base_app.models import Filial, Menu, SubMenu, Contracts
from ut.models import Goods, Agent, Invoice, InvoiceBody, Test

depth_level = None
SAFE_METHODS = ['GET', 'DELETE']


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        depth = depth_level
        fields = '__all__'


class FilialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filial
        depth = depth_level
        fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        depth = depth_level
        fields = '__all__'


class SubMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubMenu
        depth = depth_level
        fields = '__all__'


class ContractsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contracts
        depth = depth_level
        fields = '__all__'


class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        depth = depth_level
        fields = '__all__'


class InvoiceBodySerializer(serializers.ModelSerializer):
    invoice_body_goods = GoodsSerializer(many=True, read_only=True)

    class Meta:
        model = InvoiceBody
        depth = depth_level
        fields = '__all__'


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        depth = depth_level
        fields = '__all__'


class InvoiceSerializer(serializers.ModelSerializer):
    invoice_body = InvoiceBodySerializer(many=True, read_only=True)
    sum_weight_netto = serializers.SerializerMethodField()

    class Meta:
        model = Invoice
        # depth = 1
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(InvoiceSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request.method in SAFE_METHODS:
            self.Meta.depth = 1
        else:
            self.Meta.depth = 0

    @staticmethod
    def get_sum_weight_netto(obj):
        x = 0
        for i in obj.invoice_body.all():
            x += (i.quantity * i.goods_id.weight_netto)
        return x
