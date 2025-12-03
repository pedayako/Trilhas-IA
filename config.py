import os
from dotenv import load_dotenv

load_dotenv()

# Credenciais
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

# Caminhos e Modelos
PASTA_DOCUMENTS = "./documentos"
PASTA_DB = "./banco_vetorial"
NOME_COLECAO = "conhecimento_empresa"
MODELO_IA = "openai/gpt-oss-20b" # Modelo robusto para instruções