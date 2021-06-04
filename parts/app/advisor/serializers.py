from rest_framework import serializers

from parts.app.advisor.models import ServiceAdvisor


class ServiceAdvisorSerializers(serializers.ModelSerializer):
    class Meta:
        model = ServiceAdvisor
        fields = '__all__'

