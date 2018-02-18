


from django.conf.urls import url, include
from .api_views import WorkListAPIView

urlpatterns = [
    url('^$', WorkListAPIView.as_view(), name='list')
]
