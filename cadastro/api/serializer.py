from rest_framework import serializers, status
from rest_framework.response import Response
from clientes import models
import requests
import pandas as pd

from cadastro.api.validacao.nome_completo import *
from cadastro.api.validacao.cpf import *
from cadastro.api.validacao.telefone import *
from cadastro.api.validacao.cep import *

class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cliente
        fields = '__all__'



        
    def validate(self, data):
        nome = data['nome_completo']
        cpf = data['cpf'] 
        telefone = str(data['telefone'])
        cep = str(data['cep'])
        cidade = data['cidade']
        estado = data['estado']
        logradouro = data['logradouro']

        valor_nome = validando_nome(nome)
        valor_cpf = validando_cpf(cpf)
        valor_telefone = validando_telefone(telefone)
        valor_cep = validando_cep(cep, cidade, estado, logradouro)
        
        data['nome_completo'] = valor_nome
        data['cpf'] = valor_cpf
        data['telefone'] = valor_telefone
        data['cep'] = valor_cep[0]
        data['cidade'] = valor_cep[1]
        data['estado'] = valor_cep[2]
        data['logradouro'] = valor_cep[3]


        return data
        
      
        

       