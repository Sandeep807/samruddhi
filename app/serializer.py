
from django.db.models import fields
from rest_framework import serializers
from .models import *

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        exclude=['updated_at']
    # def create(self,validated_data):
    #     amount=validated_data['amount_paid']
    #     Customer.objects.create(**validated_data)


class WalletSerialiser(serializers.ModelSerializer):
    class Meta:
        model=Wallet
        fields='__all__'

class LoginSerialiser(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()


class UserSerailizer(serializers.ModelSerializer):
    wallets=WalletSerialiser(read_only=True,many=True)
    class Meta:
        model=User
        fields=['id','first_name','wallets']