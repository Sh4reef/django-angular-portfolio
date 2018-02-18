from rest_framework.generics import ListAPIView
from .models import Lab
from .serializers import LabSerializer

class LabListAPIView(ListAPIView):
    queryset = Lab.objects.all()
    serializer_class = LabSerializer
