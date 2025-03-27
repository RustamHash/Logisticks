from django.urls import path

from .views import FilialAPIView

app_name = "api"


urlpatterns = [
    path('api/v1/filials/', FilialAPIView.as_view(), name='filials')
]