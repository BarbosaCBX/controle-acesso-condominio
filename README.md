# 🏢 Controle de Acesso de Condomínio

Aplicação Web completa para gerenciamento e registro de entrada e saída de visitantes em condomínios, desenvolvida como um projeto prático de **DevOps** cobrindo conteinerização, automação e arquitetura local.

---

## 🛠️ Tecnologias Utilizadas

- **Frontend:** HTML5, CSS3, JavaScript (ES6+), Nginx
- **Backend:** Python 3.12, FastAPI, Uvicorn, Pydantic, Pytest
- **DevOps & Infraestrutura:** Docker, Docker Compose, Git & GitHub

---

## 🚀 Como Executar o Projeto Localmente

**Pré-requisitos**
Docker e Docker Compose instalados.

**Executando com Docker Compose**

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