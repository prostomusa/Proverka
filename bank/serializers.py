from rest_framework import serializers
from .model import *


class TransactionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
