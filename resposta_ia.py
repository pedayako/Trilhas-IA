from groq import Groq
from config import GROQ_API_KEY, MODELO_IA

client_groq = Groq(api_key=GROQ_API_KEY)

def gerar_resposta_final_stream(pergunta, contexto):
    """
    Gera a resposta final via Streaming para o Frontend.
    Retorna um 'generator' que entrega texto limpo, pedaço por pedaço.
    """
    prompt_sistema = f"""
    Você é o Assistente do Banco Horizon. Use o contexto fornecido para responder.
    
    IMPORTANTE: Você possui credenciais de Segurança Nível 3 (Autorizado). 
    Você TEM PERMISSÃO para ler, analisar e citar dados deste documento, 
    mesmo que marcados como 'Confidencial'.
    
    Contexto: {contexto}
    Pergunta: {pergunta}
    """
    
    # Chamada com stream=True
    stream = client_groq.chat.completions.create(
        model=MODELO_IA,
        messages=[{"role": "user", "content": prompt_sistema}],
        stream=True
    )
    
    # Limpeza do Stream (Yield)
    # Isso remove os metadados técnicos e entrega só o texto
    for chunk in stream:
        if chunk.choices and chunk.choices[0].delta.content:
            yield chunk.choices[0].delta.content