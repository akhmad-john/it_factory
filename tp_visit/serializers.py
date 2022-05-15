from rest_framework import serializers

from .models import Visit


class VisitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = (
            'id',
            'trade_point_id',
            'latitude',
            'longitude',
            'created_at'
        )

