from cadastro.api.validacao.msg.mensagem import *
def validando_nome(nome):
    
    removido_espacos = nome.replace(" ", "")
    # Validar se existem no mínimo 12 caracteres para ver se não tem apenas espaços em branco ou se é um nome
    if len(removido_espacos) < 12:
        valor_menor('Nome Completo', 12, len(removido_espacos))
        


    apenas_letras = removido_espacos.isalpha()
    # Validar se o número contem algum caracter especial, se tiver, o if infomra para o clientes
    if apenas_letras == False:
        apenas_letras_valor('Nome Completo',nome)



    # Valida se existe no mínimo 2 espaços devído ao 2 sobrenomes após o nome, caso o cliente tenha 2 nomes ex:joão vitor, ainda assim vai pedir mais o sobrenome 
    contar_espacos = nome.count(' ')
    if contar_espacos < 2:
        quatidade_espacos(nome)

    

    # Aqui estamos formatando a letra para deixar todas as primeiras letras maiusculas
    letra_maiuscula = nome.title()
    
    return letra_maiuscula

    
    