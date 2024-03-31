# Use a imagem base do Python
FROM python:3.8-slim

# Configuração do diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie o arquivo requirements.txt para o contêiner
COPY requirements.txt .

# Instale as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copie todo o conteúdo do diretório atual para o contêiner
COPY . .

# Expor a porta 8501
EXPOSE 8501

# Comando para executar o aplicativo quando o contêiner for iniciado
CMD ["streamlit", "run", "app.py", "--server.port", "8501"]
