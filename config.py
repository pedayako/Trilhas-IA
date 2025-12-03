import os
from dotenv import load_dotenv

load_dotenv()

# --- CONFIGURAÇÕES GERAIS ---
# [DESAFIO]: Garanta que sua chave esteja no arquivo .env
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

# Caminhos
PASTA_DOCUMENTS = "./documentos"
PASTA_DB = "./banco_vetorial"
NOME_COLECAO = "conhecimento_empresa"

# [DESAFIO]: Escolha um modelo suportado pela Groq (ex: llama3-70b-8192 ou mixtral-8x7b-32768)
# O modelo anterior "openai/gpt-oss-20b" era um placeholder.
MODELO_IA = "llama3-70b-8192"