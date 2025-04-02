from django.db.models import Sum
from rest_framework import generics, viewsets, status, permissions
from rest_framework.response import Response

from base_app.models import Filial, Menu, Contracts, SubMenu
from ut.models import Goods, Agent, Test, Invoice, InvoiceBody

from .serializers import FilialSerializer, MenuSerializer, SubMenuSerializer, ContractsSerializer
from .serializers import GoodsSerializer, AgentSerializer, InvoiceSerializer, InvoiceBodySerializer, TestSerializer


class TestViewSet(generics.ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class FilialAPIView(generics.ListAPIView):
    queryset = Filial.objects.filter(as_active=True)
    serializer_class = FilialSerializer


class ContractsAPIView(generics.ListAPIView):
    queryset = Contracts.objects.filter(as_active=True)
    serializer_class = ContractsSerializer


class ContractsAPIViewDetail(generics.RetrieveAPIView):
    queryset = Contracts.objects.filter(as_active=True)
    serializer_class = ContractsSerializer


class MenuAPIView(generics.ListAPIView):
    queryset = Menu.objects.filter(as_active=True)
    serializer_class = MenuSerializer


class SubMenuAPIView(generics.ListAPIView):
    queryset = SubMenu.objects.filter(as_active=True)
    serializer_class = SubMenuSerializer


class SubMenuAPIViewDetail(generics.ListAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer


class GoodsAPIView(generics.ListCreateAPIView):
    queryset = Goods.objects.filter()
    serializer_class = GoodsSerializer


class GoodsAPIViewDetail(generics.RetrieveAPIView):
    queryset = Goods.objects.filter()
    serializer_class = GoodsSerializer


class AgentListAPIView(generics.ListCreateAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer


class AgentDetailAPIView(generics.RetrieveAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer


class InvoiceAPIView(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class InvoiceDetailAPIView(generics.RetrieveAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class InvoiceBodyAPIViewDetail(generics.RetrieveAPIView):
    queryset = InvoiceBody.objects.all()
    serializer_class = InvoiceBodySerializer


class InvoiceBodyListAPIView(generics.ListCreateAPIView):
    queryset = InvoiceBody.objects.all()
    serializer_class = InvoiceBodySerializer
