from rest_framework import serializers, status
from rest_framework.response import Response


error_400_status = code=status.HTTP_400_BAD_REQUEST
sucess_200_status = code=status.HTTP_200_OK
# Letras
def valor_menor(nome, valor, qtd):
    raise serializers.ValidationError('VALOR INVÁLIDO: O valor {} deve conter no mínimo {} caracteres para que possa prosseguir! Quantidade de Caracteres inseridos {} .'.format(nome, str(valor), qtd), error_400_status) #code=status.HTTP_400_BAD_REQUEST3

def apenas_letras_valor(nome, valor):
    raise serializers.ValidationError('VALOR INVÁLIDO: O {} deve conter apenas letras, não podendo ser utilizado caracteres ou números! valor inserido {} .'.format(nome, valor), error_400_status)

def quatidade_espacos(valor):
    raise serializers.ValidationError('VALOR INVÁLIDO: Você dever inserir seu nome completo! Valor inserido: {}'.format(valor), error_400_status) 

def quatidade_espacos(valor):
    raise serializers.ValidationError('VALOR INVÁLIDO: Você dever inserir seu nome completo! Valor inserido: {}'.format(valor), error_400_status) 


# Números
def apenas_numeros_valor(nome, valor):
    raise serializers.ValidationError('VALOR INVÁLIDO: O {} deve conter apenas números, não podendo ser utilizado letras ou caracteres divergentes do {}! Valor inserido: {}'.format(nome, nome, valor), error_400_status) 

def quantidade_caracteres(qtd, nome, valor):
    raise serializers.ValidationError('VALOR INVÁLIDO: Você dever inserir {} digitos númericos no campo {}! Valor inserido: {} caracteres'.format(str(qtd), nome, valor), error_400_status) 

def quantidade_entre_numero_valor(nome, valor, v1, v2):
    raise serializers.ValidationError('VALOR INVÁLIDO: {} deve ter um número maior que {} caracteres e menor que {} caracteres! Valor inserido: {} caracteres'.format(nome, str(v1), str(v2), valor), error_400_status) 



# CEP
def validacao_cidade_estado(cidade, estado):
    raise serializers.ValidationError('VALOR INVÁLIDO: A cidade informada não consta no estado selecionado, inserir cidade válida! Cidade: {}, Estado: {}'.format(cidade, estado), error_400_status)

def estado_cep_invalido(nome, valor):
    raise serializers.ValidationError(
            'VALOR INVÁLIDO: O {} inserido não foi encontrado! Valor inserido: {}'.format(nome, valor), error_400_status)

def verificacao_cep(nome, valor, valor_cep):
    raise serializers.ValidationError(
        'VALOR INVÁLIDO: Valor {} está divergente do valor CEP! Valor inserido: {}, Valor do CEP: {}'.format(nome, valor, valor_cep), error_400_status)

def divergencia_valores(cep, cidade, estado, logradouro):
    raise serializers.ValidationError(
                        'VALOR INVÁLIDO: Favor verificar as infomações inseridas CEP: {}, Cidade: {}, Estado: {} e Logradouro: {}'.format(cep, cidade, estado, logradouro), error_400_status)

# 200 OK

def valor_validado(nome, valor):
    return Response('{} Válidado {} !'.format(nome, valor), sucess_200_status)

def valor_validado_cep(cep, cidade, estado, logradouro):
    return Response('CEP: {}, Cidade: {}, Estado: {} e Logradouro: {} Válidados!'.format(cep, cidade, estado, logradouro), sucess_200_status)