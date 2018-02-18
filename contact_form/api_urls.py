

from django.conf.urls import url
from .api_views import ContactFormAPIView

urlpatterns = [
    url('^$', ContactFormAPIView.as_view(), name='form')
]