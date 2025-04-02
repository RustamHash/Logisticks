from django.urls import path
from rest_framework import routers

from .views import (FilialAPIView, ContractsAPIView, ContractsAPIViewDetail, MenuAPIView, SubMenuAPIView,
                    AgentListAPIView, InvoiceAPIView,InvoiceDetailAPIView, AgentDetailAPIView, TestViewSet,
                    GoodsAPIView, GoodsAPIViewDetail, InvoiceBodyAPIViewDetail, InvoiceBodyListAPIView)

app_name = "api"
router = routers.DefaultRouter()

# router.register(r'tests/', TestViewSet)

urlpatterns = [
    path('filials/', FilialAPIView.as_view(), name='filials'),
    path('contracts/', ContractsAPIView.as_view(), name='contracts'),
    path('contracts/<int:pk>', ContractsAPIViewDetail.as_view(), name='contract'),
    path('menus/', MenuAPIView.as_view(), name='menus'),
    path('submenus/', SubMenuAPIView.as_view(), name='submenus'),
    path('agents/', AgentListAPIView.as_view(), name='agents'),
    path('agent/<int:pk>', AgentDetailAPIView.as_view(), name='agents'),
    path('invoices/', InvoiceAPIView.as_view(), name='invoices'),
    path('invoices/<int:pk>', InvoiceDetailAPIView.as_view(), name='invoices'),
    path('goods/', GoodsAPIView.as_view(), name='goods'),
    path('goods/<int:pk>', GoodsAPIViewDetail.as_view(), name='goods'),
    path('invoice_body/', InvoiceBodyListAPIView.as_view(), name='invoice_body'),
    path('invoice_body/<int:pk>', InvoiceBodyAPIViewDetail.as_view(), name='invoice_body'),
    path('tests/', TestViewSet.as_view(), name='tests'),
]
