
# Especificação de caso de uso
## Cloud-PRISM Back End
#### Objetivo geral:
Executar e retornar resultados do modelo com suas propriedades e variaveis geradas no ambiente de desenvolvimento front end [PRISM](https://www.prismmodelchecker.org/).


## Caso de uso: Salvar arquivos para execução
#### Descrição:
Gerar arquivos de modelo e propriedades para chamada do comando do compilador PRISM.

#### Pré-condição:
Envio dos códigos de modelo e propriedades pelo frontend.

#### Pós-condição:
Gerar comando para execução do modelo.


## Caso de uso: Executar o modelo
#### Descrição:
Executar o modelo com o comando da aplicação prism com os arquivos gerados pelos códigos e as variaveis de execução.

#### Pré-condição:
Criação dos arquivos de modelo e propriedades, assim como o comando de execução.
#### Pós-condição:
Retornar o resultado da execução do modelo.


## Caso de uso: Retornar resultado da execução do modelo
#### Descrição:
Retornar o resultado positivo ou de erro da execução do modelo.

#### Pré-condição:
Execução bem sucedida ou não da execução do modelo criado enviado pelo front end.

#### Pós-condição:
Retorno completo do resultado da execução e finalização do processo.
