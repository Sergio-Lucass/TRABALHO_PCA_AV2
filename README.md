# SISTEMA DE GERENCIAMENTO QUE CADASTRA INFS BÁSICAS DE ALUNOS (AV2 - PCA)

## NOME DO DESENVOLVEDOR: Sérgio Lucas Gomes da Silva Rodrigues

## Descrição do Projeto

Este projeto é um sistema simples de gerenciamento de dados de alunos, desenvolvido em Python. Ele utiliza a biblioteca *OS* que verifica a existência do arquivo CSV e a do *Pandas* para persistência de dados, salvando e carregando todas as informações em um arquivo CSV (inf_alunos.csv).

O objetivo é cumprir os requisitos da Avaliação da AV2 da disciplina PRINCÍPIOS DE CONSTRUÇÃO DE ALGORÍTIMOS, demonstrando habilidades em funções(def), dicionários (dict), vetores (list), loops(for/while), condições(if,elif,else) e na gravação de todas as informações em arquivo (pandas dataframe).

## Funcionalidades

O menu principal oferece as seguintes opções:

* *1 - INSERIR:* Cadastra um novo aluno. A matrícula é gerada *automaticamente* e sequencialmente (criar_matricula).
* *2 - PESQUISAR:* Permite buscar os dados do aluno de acordo com sua Matrícula ou Nome (neste código a busca por nome é *case-insensitive*).
    * Após a pesquisa e seleção, o usuário pode optar por *EDITAR* ou *REMOVER* o registro ou simplesmente voltar para o *MENU*.
* *3 - SAIR:* Finaliza o programa, solicitando uma confirmação ao usuário.

## 🛠️ Requisitos e Como Executar

### 1. Requisitos para Usar o Programa
* *Python 3.x*
* *Pandas:* Biblioteca utilizada para manipulação de DataFrames e leitura/escrita de CSV.
* *OS:* Biblioteca utilizada para verificar a existência do arquivo CSV antes de tentar carregá-lo.

### 2. Instalação
Abra o terminal na pasta do projeto e instale a dependência necessária:

```bash
pip install pandas