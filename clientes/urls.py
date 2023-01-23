from django.urls import path

from .views import ClienteAPIView, ClientesAPIView

urlpatterns = [
    path('clientes/', ClientesAPIView.as_view(), name='clientes'),
    path('clientes/<int:pk>', ClienteAPIView.as_view(), name='cliente')
]