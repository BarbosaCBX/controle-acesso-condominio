# 🏢 Controle de Acesso de Condomínio

Aplicação Web completa para gerenciamento e registro de entrada e saída de visitantes em condomínios, desenvolvida como um projeto prático de **DevOps** cobrindo conteinerização, automação e arquitetura local.

---

## 🛠️ Tecnologias Utilizadas

- **Frontend:** HTML5, CSS3, JavaScript (ES6+), Nginx
- **Backend:** Python 3.12, FastAPI, Uvicorn, Pydantic, Pytest
- **DevOps & Infraestrutura:** Docker, Docker Compose, Git & GitHub

---

## 🚀 Como Executar o Projeto Localmente

### Pré-requisitos
Docker e Docker Compose instalados.

### Executando com Docker Compose

* **1. Clone o Repositório:**
    ```bash
    git clone [https://github.com/BarbosaCBX/controle-acesso-condominio.git](https://github.com/BarbosaCBX/controle-acesso-condominio.git)
    cd controle-acesso-condominio

* **2. Suba o ambiente unificado:**

    ```bash
    docker compose up --build -d

* **3. acesse no seu navegador:**
    **Frontend (Portaria):** http://localhost

    **Documentação da API (Swagger):** http://localhost:8000/docs

    **Healthcheck:** http://localhost:8000/health

---

## 🛠️ Solução de Problemas (Troubleshooting)

### 🚨 1. Erro no Push do Git (`non-fast-forward` / `updates were rejected`)

- **Causa:** O repositório no GitHub continha commits ou arquivos iniciais que não existiam no ambiente local.
- **Solução:** Sincronize os históricos permitindo mesclar commits não relacionados antes de enviar:
  ```bash
  git pull origin main --allow-unrelated-histories --no-rebase
  git push -u origin main

### 🚨 2. Pytest não encontra o módulo `app` (`ModuleNotFoundError`)

- **Causa:** O Python não incluiu o diretório atual do backend no caminho de busca de módulos (`PYTHONPATH`).
- **Solução:** Defina explicitamente o `pythonpath` no arquivo `backend/pytest.ini` ou passe a variável de ambiente na execução:
  ```bash
  PYTHONPATH=. pytest

### 🚨 3. Falha de dependência do container backend no Docker Compose

- **Causa:** O teste de saúde (`healthcheck`) tentou utilizar o comando `curl`, inexistente na imagem base `python:3.12-slim`.
- **Solução:** Substitua a chamada `curl` no `docker-compose.yml` usando o próprio módulo interno `urllib.request` do Python:
  ```yaml
  healthcheck:
    test: ["CMD", "python", "-c", "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')"]

