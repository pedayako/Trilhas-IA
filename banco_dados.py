import chromadb
from config import PASTA_DB, NOME_COLECAO

# Inicializa o cliente uma única vez
client = chromadb.PersistentClient(path=PASTA_DB)
colecao = client.get_or_create_collection(name=NOME_COLECAO)

def salvar_no_banco(texto, nome_arquivo):
    """Salva um documento no banco vetorial."""
    colecao.upsert(
        documents=[texto],
        ids=[nome_arquivo],
        metadatas=[{"origem": nome_arquivo}]
    )

def buscar_contexto(pergunta):
    """Busca o trecho mais relevante (n=1)."""
    resultado = colecao.query(
        query_texts=[pergunta], 
        n_results=1
    )
    
    if resultado['documents'] and resultado['documents'][0]:
        return resultado['documents'][0][0] # Retorna string pura
    return ""