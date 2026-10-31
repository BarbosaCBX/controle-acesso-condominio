FROM python:3.12-slim

# Define o diretório de trabalho
WORKDIR /app

# Impede o Python de escrever arquivos .pyc no disco e habilita logs em tempo real
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Instala as dependências primeiro (aproveitamento de cache do Docker)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação
COPY ./app ./app

# Cria um usuário sem privilégios de root para segurança
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 8000

# Executa o Uvicorn apontando para a aplicação FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]