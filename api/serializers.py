from rest_framework import serializers
from base_app.models import Filial, Menu


class FilialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filial
        fields = '__all__'
