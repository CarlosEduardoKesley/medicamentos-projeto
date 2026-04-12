 
#  Controle de Medicamentos CLI

[![Pipeline CI](https://github.com/CarlosEduardoKesley/medicamentos-projeto/actions/workflows/ci.yml/badge.svg)](https://github.com/CarlosEduardoKesley/medicamentos-projeto/actions/workflows/ci.yml)

## 1. Descrição do Problema Real
Muitos cuidadores de idosos lidam com rotinas exaustivas e múltiplas medicações. A confusão nos horários e dosagens é uma dor real que coloca a saúde do paciente em risco.

## 2. Proposta da Solução
Uma aplicação simples via terminal (CLI) para registrar e consultar os horários de medicamentos de forma rápida e direta.

## 3. Público-alvo
Cuidadores familiares ou profissionais de pessoas idosas ou com doenças crônicas.

## 4. Funcionalidades Principais
* Cadastro de medicamentos com nome e horário.
* Listagem formatada de medicamentos cadastrados.
* Validação de campos obrigatórios em branco.

## 5. Tecnologias Utilizadas
* Python 3.11+ (Linguagem Principal)
* Pytest (Testes Automatizados)
* Ruff (Linting / Análise Estática)
* GitHub Actions (Integração Contínua)

## 6. Instruções de Instalação
1. Clone o repositório: `git clone https://github.com/CarlosEduardoKesley/medicamentos-projeto.git`
2. Acesse a pasta do projeto: `cd medicamentos-cli`
3. Instale as dependências: `pip install -e .[dev]`

## 7. Instruções de Execução
Execute o comando no terminal:
`python src/main.py`

## 8. Instruções para Rodar os Testes
Execute o comando no terminal:
`pytest tests/`

## 9. Instruções para Rodar o Lint
Execute o comando no terminal:
`ruff check .`

## 10. Versão Atual
**1.0.0** (Versionamento Semântico MAJOR.MINOR.PATCH)

## 11. Autor
Carlos Eduardo Kesley de Oliveira Fernandes

## 12. Link do Repositório Público
https://github.com/CarlosEduardoKesley

## 13. Evidência de Funcionamento
![alt text](image.png)