from django.urls import path

from moon.views import index


urlpatterns = [
    path('', index, name='index'),
]
