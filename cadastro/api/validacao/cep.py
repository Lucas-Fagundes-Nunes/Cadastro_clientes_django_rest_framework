from cadastro.api.validacao.msg.mensagem import *
def validando_cep(cep, cidade, estado, logradouro):
    import requests
    from rest_framework import serializers, status
    from rest_framework.response import Response
    import pandas as pd

    requisicao = requests.get('https://servicodados.ibge.gov.br/api/v1/localidades/estados/{}/municipios'.format(estado))
    if requisicao.status_code == 200:
        dic_requisicao = requisicao.json()

        tabelaCidades = pd.DataFrame(dic_requisicao)
        nome_cidade = tabelaCidades['nome']

        # Validar se a cidade está no estado selecionado, caso não esteja, retorna uma mensagem informando para digitar uma cidade referente ao estado
        i = 0
        for c in nome_cidade:
            i +=1
            quantidade = nome_cidade.count()
            cidade_letras_minusculas = c.lower()
            cidade_principal_letras_minusculas = cidade.lower()
            if cidade_letras_minusculas == cidade_principal_letras_minusculas:
                # Encontrou a cidade
                break
                
            if i == quantidade:
                validacao_cidade_estado(cidade, estado)

            
    else:
        estado_cep_invalido('Estado', estado)
            


    validar_traco = cep.count('-')
    validar_espaco = cep.count(' ')
    # Validar CEP, retirar os caracteres - ou espaço, para ser buscado pela API viaCep
    if validar_traco > 0 or validar_espaco > 0:
        cep = cep.replace("-", "")
        cep = cep.replace(" ", "")

    # Validar para verificar se tem apenas números 
    if cep.isnumeric() == False:
        apenas_numeros_valor('CEP', cep)

    cep_caracteres = len(str(cep))
    # Verificar se a númeração está entre 8 e 13 o padrão (0000 0000) até (00)
    if cep_caracteres != 8:
        quantidade_caracteres(8, 'CEP', cep_caracteres)



    # Validar CEP
    viaCep = requests.get('https://viacep.com.br/ws/{}/json/'.format(str(cep)))
    print(viaCep.status_code)
    if viaCep.status_code == 200:
        try:
            resposta = viaCep.json()
            cidade_resposta = resposta['localidade']
            estado_resposta = resposta['uf']
            logradouro_resposta = resposta['logradouro']
    
            if cidade.lower() != cidade_resposta.lower():
                verificacao_cep('Cidade', cidade, cidade_resposta)
            elif estado.lower() != estado_resposta.lower():
                verificacao_cep('Estado', estado, estado_resposta)
            elif len(logradouro_resposta) > 2:
                if(logradouro_resposta.lower() != logradouro.lower()):
                    verificacao_cep('Logradouro', logradouro, logradouro_resposta)
                else:
                    return [cep, cidade, estado, logradouro]
            else: 
                return [cep, cidade, estado, logradouro]
        except:
            divergencia_valores(cep, cidade, estado, logradouro)
    else:
        estado_cep_invalido('CEP', cep)





