
from rest_framework.serializers import ModelSerializer
from .models import Lab

class LabSerializer(ModelSerializer):
    class Meta:
        model = Lab
        fields = (
                'id',
                'name',
                'description',
                'updated',
                'timestamp'
            )