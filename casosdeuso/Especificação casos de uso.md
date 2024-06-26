# Especificação de caso de uso
## Cloud-PRISM
#### Objetivo geral:
Desenvolver aplicação web com um ambiente de desenvolvimento da linguagem de análise e modelagem probabilística [PRISM](https://www.prismmodelchecker.org/).


## Caso de uso: Criar/Editar modelo
#### Descrição:
Editor de texto com realce de sintaxe, para criação do modelo probabilístico na linguagem PRISM.

#### Ator:
Usuário.

#### Pré-condição:
Acessar a página principal da aplicação.

#### Pós-condição:
Gerar resultados do modelo probabilístico.


## Caso de uso: Criar/editar propriedades
#### Descrição:
Editor de texto com realce de sintaxe, para criação das propriedades do modelo probabilístico na linguagem PRISM.

#### Ator:
Usuário.

#### Pré-condição:
Acessar a página principal da aplicação e criar um modelo no editor de texto de modelo.

#### Pós-condição:
Gerar resultados do modelo probabilístico utilizando essas propriedades.


## Caso de uso: Definir variáveis para execução do modelo
#### Descrição:
Campo de texto para definição das variáveis do modelo.

#### Ator:
Usuário.

#### Pré-condição:
Acessar a página principal da aplicação e criar um modelo e propriedades nos respectivos editores de texto.

#### Pós-condição:
Gerar resultados do modelo probabilístico utilizando essas variáveis.

## Caso de uso: alternar modo escuro

#### Descrição:
Botão de alternação da palheta de cores da página entre cores claras e escuras.

#### Ator:
Usuário.

#### Pré-condição:
Acessar a página principal da aplicação.

#### Pós-condição:
Alternar a palheta de cores da página entre cores claras e escuras.


## Caso de uso: Exibir resultados
#### Descrição:
Exibir os resultados da excecução do modelo em texto.

#### Ator:
Usuário.

#### Pré-condição:
Enviar o modelo probabilístico com ou sem propriedades e variáveis.
