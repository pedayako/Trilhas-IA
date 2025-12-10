import os
from pypdf import PdfReader
from docx import Document
from config import PASTA_DOCUMENTS
from banco_dados import salvar_no_banco

def extrair_texto(caminho):
    """Lê o arquivo e retorna o texto bruto."""
    ext = os.path.splitext(caminho)[1].lower()
    try:
        if ext == ".pdf":
            # Filtra páginas vazias para evitar erros
            return "\n".join([p.extract_text() for p in PdfReader(caminho).pages if p.extract_text()])
        elif ext == ".docx":
            return "\n".join([p.text for p in Document(caminho).paragraphs])
        elif ext == ".txt":
            with open(caminho, 'r', encoding='utf-8') as f: return f.read()
    except Exception as e:
        print(f"Erro ao ler {caminho}: {e}")
    return None

def dividir_texto(texto, tamanho_chunk=1000, overlap=200):
    """
    Divide o texto em pedaços com sobreposição.
    Essencial para evitar erro de limite de tokens.
    """
    chunks = []
    inicio = 0
    while inicio < len(texto):
        fim = inicio + tamanho_chunk
        chunks.append(texto[inicio:fim])
        # Avança com sobreposição para manter o contexto entre cortes
        inicio += tamanho_chunk - overlap
    return chunks

def executar_ingestao():
    print(f"\n--- Iniciando Ingestão em '{PASTA_DOCUMENTS}' ---")
    if not os.path.exists(PASTA_DOCUMENTS):
        os.makedirs(PASTA_DOCUMENTS)
        return

    arquivos = os.listdir(PASTA_DOCUMENTS)
    if not arquivos:
        print("Pasta vazia.")
        return

    for arquivo in arquivos:
        caminho = os.path.join(PASTA_DOCUMENTS, arquivo)
        texto_completo = extrair_texto(caminho)
        
        if texto_completo:
            print(f"Processando: {arquivo}...")
            
            # 1. Aplica o Chunking
            lista_chunks = dividir_texto(texto_completo)
            
            # 2. Envia a lista de pedaços para o módulo de banco de dados
            salvar_no_banco(lista_chunks, arquivo)
            
            print(f"  -> {len(lista_chunks)} fragmentos salvos.")
            
    print("--- Banco Atualizado ---")