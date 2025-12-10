import chromadb
from config import PASTA_DB, NOME_COLECAO

# Inicializa o cliente uma única vez
client = chromadb.PersistentClient(path=PASTA_DB)
colecao = client.get_or_create_collection(name=NOME_COLECAO)

def salvar_no_banco(lista_chunks, nome_arquivo):
    """
    Salva uma LISTA de fragmentos no banco vetorial.
    Gera IDs únicos para cada fragmento.
    """
    # Cria IDs únicos: arquivo.pdf_part_0, arquivo.pdf_part_1...
    ids = [f"{nome_arquivo}_part_{i}" for i in range(len(lista_chunks))]
    
    # Cria metadados para saber a origem de cada pedaço
    metadatas = [{"origem": nome_arquivo, "parte": i} for i in range(len(lista_chunks))]

    # Upsert aceita listas diretamente
    colecao.upsert(
        documents=lista_chunks,
        ids=ids,
        metadatas=metadatas
    )

def buscar_contexto(pergunta):

    resultado = colecao.query(
        query_texts=[pergunta], 
        n_results=3  # Aumentamos para 3 para ter mais contexto
    )
    
    if resultado['documents'] and resultado['documents'][0]:
        # Junta os 3 pedaços encontrados com uma quebra de linha visual
        return "\n\n---\n\n".join(resultado['documents'][0])
        
    return ""