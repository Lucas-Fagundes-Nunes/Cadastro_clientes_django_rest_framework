from cadastro.api.validacao.msg.mensagem import *
def validando_telefone(telefone):

    telefone_p1 = telefone.count('(')
    telefone_p2 = telefone.count(')')
    telefone_espaco = telefone.count(' ')
    telefone_traco = telefone.count('-')
    telefone_mais = telefone.count('+')
    # Verificar se o telefoe tem os seguinte caracteres (), -, + ou espaço, caso tenha, vai fazer um replace deixando apenas números
    if telefone_p1 > 0 or telefone_p2 > 0 or telefone_traco > 0 or telefone_espaco > 0 or telefone_mais > 0:
        telefone = telefone.replace("(", "")
        telefone = telefone.replace(")", "")
        telefone = telefone.replace("-", "")
        telefone = telefone.replace(" ", "")
        telefone = telefone.replace("+", "")

    # Verificar se existe alguma letra ou caracter diferente de números
    if telefone.isnumeric() == False:
        apenas_numeros_valor('Telefone', telefone)

    telefone_caracteres = len(str(telefone))
    # Verificar se a númeração está entre 8 e 13 o padrão (0000 0000) até (00)
    if telefone_caracteres < 8 or telefone_caracteres > 13:
        quantidade_entre_numero_valor('Telefone', telefone_caracteres, 8, 13)
    
    
    return telefone
    
    