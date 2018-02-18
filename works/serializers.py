

from rest_framework.serializers import ModelSerializer
from .models import Work

class WorkSerializer(ModelSerializer):
    class Meta:
        model = Work
        fields = (
                'id',
                'name',
                'description',
                'updated',
                'timestamp'
            )