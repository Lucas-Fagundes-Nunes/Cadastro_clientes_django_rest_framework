from rest_framework import generics
from .models import Cliente
from cadastro.api.serializer import ClientesSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

# GET / POST
class ClientesAPIView(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClientesSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['id', 'nome_completo', 'cpf']
    filterset_fields = ['id', 'nome_completo', 'cpf']
    

# PUT / DELETE
class ClienteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClientesSerializer
    
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['id', 'nome_completo', 'cpf']
    filterset_fields = ['id', 'nome_completo', 'cpf']