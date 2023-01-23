from cadastro.api.validacao.msg.mensagem import *
def validando_cpf(cpf):
    # Foi utilizado a biblioteca para validação de cpf no models

    validar_traco = cpf.count('-')
    validar_ponto = cpf.count('.')
    # Verifica se tem algum ponto ou traço e remove para que fique apenas a numeração do cpf, ficando padrão no banco
    if validar_traco > 0 or validar_ponto > 0:
        cpf = cpf.replace("-", "")
        cpf = cpf.replace(".", "")
  
    # Após ser verificado e ajustado o traço e os pontos, deve ser analisado se existe apenas números ou contem algum caracter inadequado
    if cpf.isnumeric() == False:
        apenas_numeros_valor('CPF', cpf)

    cpf_caracteres = len(str(cpf))
    # Verificar se a númeração está entre 8 e 13 o padrão (0000 0000) até (00)
    if cpf_caracteres != 11:
        quantidade_caracteres(11, 'CPF', cpf_caracteres)

    
    return cpf
 
    