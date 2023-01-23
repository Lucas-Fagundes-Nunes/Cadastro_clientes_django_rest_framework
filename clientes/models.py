from django.db import models
from uuid import uuid4
from cpf_field.models import CPFField


import requests
import pandas as pd

requisicao = requests.get('https://servicodados.ibge.gov.br/api/v1/localidades/estados/RS/municipios')
dic_requisicao = requisicao.json()
tabelaCidades = pd.DataFrame(dic_requisicao)

nome_cidade = tabelaCidades['nome']




# Create your models here.

class Cliente(models.Model):
    CIDADE_CHOICES = []
    for cidade in nome_cidade:
        CIDADE_CHOICES.append(cidade)
    
    
    ESTADOS_CHOICES = (
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins'),
    ('DF', 'Distrito Federal'),
    )

    SEXO_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("N", "Nenhuma das opções")
    )


    nome_completo = models.CharField(max_length=50, help_text='Nome Completo')
    cpf = CPFField('cpf', help_text='000.000.000-00',unique=True)
    telefone = models.CharField(max_length=16, help_text='(00) 0 0000-0000')
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=False, null=False, help_text='Sexo')
    cep = models.CharField(max_length=9, help_text='01001-000')
    estado = models.CharField(max_length=2, choices=ESTADOS_CHOICES, blank=False, null=False, help_text='RS / SC')
    cidade = models.CharField(max_length=150, help_text='Camaquã/ Pelotas')
    logradouro = models.CharField(max_length=50, help_text='Casa / Hotel')
    data_cadastrado = models.DateField(auto_now_add=True)
    data_atualizado = models.DateField(auto_now=True)