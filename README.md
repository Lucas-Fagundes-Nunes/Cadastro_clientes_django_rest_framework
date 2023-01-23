# PROJETO API CADASTRO CLIENTES ( DJANGO REST FRAMEWORK )

### Requisitos
* Nome completo
* CPF
* Telefone
* Sexo
* CEP
* Cidade
* Estado
* Logradouro


### Visão Geral
> Banco de dados utilizado Mysql;

> Django Rest Framework foi o framework utilizado para contruir a API;

> As operações que a API utiliza são: GET, POST, PUT e DELETE;

> Consula de cliente por chave id, CPF e Nome;

> Para cadastrar ou atualizar os valores da API, foi utilizado a API viaCep para válidar o CEP do cliente;


### Validações por Campos
##### **Nome Completo**
> Criado um arquivo específico para validações.

* É removido todos os espaços do nome e após isso é validado quantos caracteres existem, se tiver menos que 12 é informado.

* Validação de caracteres especiais, foi utilizado a função isalpha, para validar se são apenas letrar ou contem outros tipos de caracteres.

* Validação para verificar se contem menos de 2 espaços atráves do count, caso tiver, informará a mensagem de que está faltando o sobrenome.

* No final das validações o nome é formatado, deixando todas as primeiras letras maíusculas e retorna o valor.


##### **CPF**
> Criado um arquivo específico para validações.

* Utilizado a biblioteca CPFField para validação no models.

* Verifica se tem algum ponto '.' ou traço '-', caso tenha, remove.

* Valida se existe apenas números, caso tenha letras ou algum caracter especial, informa.

* Valida se existe 11 dígitos.


##### **Telefone**
> Criado um arquivo específico para validações.

* Verifica se o telefone tem algum dos seguintes caracteres: ( ) - + e 'espaço', caso tenha, é removido formatando o telefone.

* Valida se existe apenas números, caso tenha letras ou algum caracter especial, informa.

* Valida se o número de caracteres é maior que 8 e menor que 13.


##### **CEP** **Estado** **Cidade** **Logradouro**
> Criado um arquivo específico para validações.

* `Estado e Cidade :` Usado a função request, é validado primeiro o estado e a cidade, inserido o valor na requisição https://.../RS/... para pegar todas as cidades relacionadas ao estado após isso, foi utilizado a bibliote pantas para filtrar apenas as cidades, criado uma coluna. Após isso é percorrido cada nome das cidades e comparado com o nome que foi enviado (cidade), caso encontre a cidade, saí do for, se não, informa que não encontrou a cidade no estado.

* `CEP :` Verifica se tem algum ponto '.' ou traço '-', caso tenha, remove.

* `CEP :` Valida se existe apenas números, caso tenha letras ou algum caracter especial, informa.

* `CEP :` Valida se existe 8 dígitos.

* `CEP, Estado, Cidade, Logradouro :` Usado a função request para fazer um get na API viaCep, Verifica, se o cep, estado, cidade e logradouro informados estão corretos, caso não, informa.  

### Funções de Válidação
> Foram criadas algumas funções para enviar mensagens de resposta, como o código seria com as mesmas caracteristicas e teria que alterar apenas o nome e valor, foi criada essas funções de validação para deixar o código mais legivel e limpo;

