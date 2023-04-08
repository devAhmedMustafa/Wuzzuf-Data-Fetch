from django.urls import path
from . import views



urlpatterns = [
    path('', views.app, name='app'),
    path('fetch/wuzzuf/', views.fetch_request),
    path('dw', views.download, name='download')
]
