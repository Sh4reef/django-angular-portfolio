

from django.conf.urls import url, include

urlpatterns = [
    url('^contact/', include('contact_form.api_urls', namespace='contact')),
    url('^labs/', include('labs.api_urls', namespace='labs')),
    url('^works/', include('works.api_urls', namespace='works'))
]
