from rest_framework import serializers

from parts.app.partsnumber.models import (
    PartsNumber,
    PartNumberClass,
    UnitMeasure,
    SourceCode,
    SellingPrice
)

# Serializer class for Partsnumber Model
class PartNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartsNumber
        fields = ['partnnumber', 'source_code', 'bar_code', 'selling_price',
                  'status', 'unit_measure']


# Parts Number Class Serializer
class PartNumberClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartNumberClass
        fields = ['class_name', 'charge_type']


# UnitMeasure Class Serializer
class UnitMeasureSerializer(serializers.ModelSerializer):

    # TODO: update this if there's some field in the UnitMeasure model

    class Meta:
        model = UnitMeasure
        fields = ['sku_um']


class SourceCodeSerialzer(serializers.ModelSerialzers):
    class Meta:
        model = SourceCode
        fields = ['code', 'description']


class SellingPriceSerializer(serializers.ModelSerialzer):
   
    # TODO: update this if there will be new fields in the selling price class 
    # that is important for the partnumbers model

    class Meta:
        model = SellingPrice
        fields = ['selling_price', 'discount_percentage']

