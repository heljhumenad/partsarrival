from rest_framework import serializers

from parts.app.arrival.models import PartsArrival


class PartsArrivalSerializers(serializers.ModelSerializer):
    class Meta:
        models = PartsArrival
        # When using table field as fields on Meta just use ['field_name', 'field_name2'] as
        # an argument of fields attribute
        fields = '__all__' 
