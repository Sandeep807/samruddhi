
from django.db.models import fields
from rest_framework import serializers
from .models import *

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        exclude=['updated_at']

class WalletSerialiser(serializers.ModelSerializer):
    class Meta:
        model=Wallet
        fields='__all__'

class LoginSerialiser(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()
