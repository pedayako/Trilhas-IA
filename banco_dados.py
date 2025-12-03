import chromadb
from config import PASTA_DB, NOME_COLECAO

try:
    client = chromadb.PersistentClient(path=PASTA_DB)
    colecao = client.get_or_create_collection(name=NOME_COLECAO)
except:
    colecao = None

def salvar_no_banco(texto, nome_arquivo):
    if colecao:
        colecao.upsert(documents=[texto], ids=[nome_arquivo], metadatas=[{"origem": nome_arquivo}])

def buscar_contexto(pergunta):
    if not colecao: return ""
    
    # --- ÁREA TÉCNICA (NÃO MEXER) ---
    try:
        resultado = colecao.query(
            query_texts=[pergunta], # O Chroma faz a matemática vetorial aqui
            n_results=2
        )
        
        # [MISSÃO 5]: Validação de Retorno.
        # O Chroma retorna uma lista dentro de outra lista.
        # Se tiver documentos encontrados, retorne o texto.
        
        if resultado['documents']:
             return resultado['documents'][0][0]
            
    except Exception as e:
        print(f"Erro na busca: {e}")
    # --------------------------------
    
    return ""