# 💊 MedCuidar — Controle de Medicamentos

[![Pipeline CI](https://github.com/CarlosEduardoKesley/medicamentos-projeto/actions/workflows/ci.yml/badge.svg?branch=entrega-intermediaria)](https://github.com/CarlosEduardoKesley/medicamentos-projeto/actions/workflows/ci.yml)

> 🌐 **Aplicação publicada:** https://medicamentos-projeto.onrender.com

---

## 1. Descrição do Problema Real
Muitos cuidadores de idosos lidam com rotinas exaustivas e múltiplas medicações. A confusão nos horários e dosagens é uma dor real que coloca a saúde do paciente em risco.

## 2. Proposta da Solução
Uma aplicação web para registrar e gerenciar os horários de medicamentos de forma visual e intuitiva. O sistema consome a API de clima Open-Meteo para exibir alertas sobre temperatura em Brasília — ajudando o cuidador a tomar decisões como agasalhar ou hidratar o paciente antes de sair.

## 3. Público-alvo
Cuidadores familiares ou profissionais de pessoas idosas ou com doenças crônicas.

## 4. Funcionalidades Principais
* Cadastro de medicamentos com nome, horário e dose.
* Listagem ordenada por horário com cards visuais.
* Edição e remoção de medicamentos (CRUD completo).
* Alerta de clima em tempo real via API Open-Meteo (sem chave, gratuita).
* Validação de campos obrigatórios.

## 5. Tecnologias Utilizadas
* Python 3.11+ (Linguagem Principal)
* FastAPI (Framework Web)
* Jinja2 (Templates HTML)
* HTTPX (Consumo de API externa)
* Pytest + pytest-asyncio (Testes Unitários e de Integração)
* Ruff (Linting / Análise Estática)
* GitHub Actions (Integração Contínua)

## 6. API Pública Integrada
**Open-Meteo** — API gratuita e aberta de previsão do tempo.
- Endpoint: `https://api.open-meteo.com/v1/forecast`
- Dados utilizados: temperatura atual em Brasília (latitude `-15.78`, longitude `-47.93`)
- Sem necessidade de chave de autenticação

## 7. Instruções de Instalação
1. Clone o repositório:
   ```bash
   git clone https://github.com/CarlosEduardoKesley/medicamentos-projeto.git
   ```
2. Acesse a pasta do projeto:
   ```bash
   cd medicamentos-projeto
   ```
3. Instale as dependências:
   ```bash
   pip install -e ".[dev]"
   pip install python-multipart pytest-asyncio
   ```

## 8. Instruções de Execução
```bash
python -m uvicorn src.main:app --reload --port 8080
```
Acesse no navegador: `http://localhost:8080`

## 9. Instruções para Rodar os Testes
```bash
python -m pytest tests/ -v
```

## 10. Instruções para Rodar o Lint
```bash
ruff check .
```

## 11. Versão Atual
**2.0.0** (Versionamento Semântico MAJOR.MINOR.PATCH)

## 12. Autor
Carlos Eduardo Kesley de Oliveira Fernandes

## 13. Link do Repositório Público
https://github.com/CarlosEduardoKesley/medicamentos-projeto
