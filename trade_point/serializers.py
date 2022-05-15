from rest_framework import serializers

from .models import TradePoint


class TradePointSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradePoint
        fields = ('id', 'name')
