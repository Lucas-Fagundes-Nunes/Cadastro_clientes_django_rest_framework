from rest_framework import viewsets
from cadastro.api import serializer
from clientes import models
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class ClientesViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.ClientesSerializer
    queryset = models.Cliente.objects.all()

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['id', 'nome_completo', 'cpf']
    filterset_fields = ['id', 'nome_completo', 'cpf']
    