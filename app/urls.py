""" app urls """

from django.urls import path
from . import views

# Added to serve static content during DEV (DEBUG=True)
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.test, name='test'),
    path('index/', views.index, name='index'),
    path('upload/', views.upload_file, name='upload_file'),

    # this static part must be added to serve static content while DEBUG=True
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
