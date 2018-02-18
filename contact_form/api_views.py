
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from .serializers import ContactFormSerializer


class ContactFormAPIView(APIView):
    def post(self, request, format=None):
        serializer = ContactFormSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, HTTP_201_CREATED)
        return Response(serializer.data, HTTP_400_BAD_REQUEST)