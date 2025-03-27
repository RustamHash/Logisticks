from rest_framework import generics
from base_app.models import Filial, Menu
from .serializers import FilialSerializer


class FilialAPIView(generics.ListAPIView):
    queryset = Filial.objects.filter(as_active=True)
    serializer_class = FilialSerializer

