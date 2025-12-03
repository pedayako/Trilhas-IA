import os
from pypdf import PdfReader
from docx import Document
from config import PASTA_DOCUMENTS
from banco_dados import salvar_no_banco

def extrair_texto(caminho):
    ext = os.path.splitext(caminho)[1].lower()
    try:
        if ext == ".pdf":
            return "\n".join([p.extract_text() for p in PdfReader(caminho).pages])
        elif ext == ".docx":
            return "\n".join([p.text for p in Document(caminho).paragraphs])
        elif ext == ".txt":
            with open(caminho, 'r', encoding='utf-8') as f: return f.read()
    except Exception as e:
        print(f"Erro ao ler {caminho}: {e}")
    return None

def executar_ingestao():
    print(f"\n--- Iniciando Ingestão em '{PASTA_DOCUMENTS}' ---")
    if not os.path.exists(PASTA_DOCUMENTS):
        os.makedirs(PASTA_DOCUMENTS)
        return

    arquivos = os.listdir(PASTA_DOCUMENTS)
    for arquivo in arquivos:
        caminho = os.path.join(PASTA_DOCUMENTS, arquivo)
        texto = extrair_texto(caminho)
        
        if texto:
            print(f"Indexando: {arquivo}")
            salvar_no_banco(texto, arquivo)
            
    print("--- Banco Atualizado ---")