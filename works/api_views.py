from rest_framework.generics import ListAPIView
from .models import Work
from .serializers import WorkSerializer

class WorkListAPIView(ListAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer

