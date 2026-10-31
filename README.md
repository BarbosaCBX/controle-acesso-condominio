# 🏢 Controle de Acesso de Condomínio

Aplicação Web completa para gerenciamento e registro de entrada e saída de visitantes em condomínios, desenvolvida como um projeto prático de **DevOps** cobrindo conteinerização, automação e arquitetura local.

---

## 🛠️ Tecnologias Utilizadas

- **Frontend:** HTML5, CSS3, JavaScript (ES6+), Nginx
- **Backend:** Python 3.12, FastAPI, Uvicorn, Pydantic, Pytest
- **DevOps & Infraestrutura:** Docker, Docker Compose, Git & GitHub

---

## 📁 Estrutura do Projeto

```text
controle-acesso-condominio/
├── .github/
│   └── workflows/          # Pipelines de CI/CD (GitHub Actions)
├── infrastructure/         # Manifestos IaC (Terraform, Ansible, K8s)
├── backend/                # API REST em FastAPI e testes unitários
│   ├── app/                # Código fonte da API
│   ├── tests/              # Testes automatizados com Pytest
│   └── Dockerfile          # Imagem Docker do Backend
├── frontend/               # Interface Web da Portaria
│   ├── public/             # Arquivos HTML estáticos
│   ├── src/                # Estilos CSS e rotinas JavaScript
│   ├── nginx.conf          # Configuração de Proxy Reverso
│   └── Dockerfile          # Imagem Multi-Stage do Frontend
├── docker-compose.yml      # Orquestração do ambiente local
└── README.md

---

# 🚀 Como Executar o Projeto Localmente

**Pré-requisitos**
Docker e Docker Compose instalados.

**Executando com Docker Compose**

* **1. Clone o Repositório:**
    '''bash
    git clone [https://github.com/BarbosaCBX/controle-acesso-condominio.git](https://github.com/BarbosaCBX/controle-acesso-condominio.git)
    cd controle-acesso-condominio

* **2. Suba o ambiente unificado:**

    '''bash
    docker compose up --build -d

* **3. acesse no seu navegador:**
    **Frontend (Portaria):** http://localhost

    **Documentação da API (Swagger):** http://localhost:8000/docs

    **Healthcheck:** http://localhost:8000/health