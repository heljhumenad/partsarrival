from rest_framework import serializers

from parts.app.partsnumber.models import (
    PartsNumber,
    PartNumberClass,
    UnitMeasure,
)

class PartNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartsNumber
        fields = '__all__'
        
class PartNumberClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartNumberClass
        fields = '__all__'

class UnitMeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitMeasure
        fields = '__all__'