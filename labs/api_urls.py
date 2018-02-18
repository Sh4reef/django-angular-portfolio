


from django.conf.urls import url, include
from .api_views import LabListAPIView

urlpatterns = [
    url('^$', LabListAPIView.as_view(), name='list')
]