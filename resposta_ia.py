from groq import Groq
from config import GROQ_API_KEY, MODELO_IA

client_groq = Groq(api_key=GROQ_API_KEY)

def gerar_resposta_final_stream(pergunta, contexto):
    
    # [MISSÃO 6]: Crie a Persona do Assistente (RAG).
    # IMPORTANTE: Você deve incluir as variáveis {contexto} e {pergunta}.
    prompt_sistema = f"""
    
    CONTEXTO:
    {contexto}
    
    PERGUNTA:
    {pergunta}
    """

    # --- ÁREA TÉCNICA (STREAMING PRONTO) ---
    try:
        stream = client_groq.chat.completions.create(
            model=MODELO_IA,
            messages=[{"role": "user", "content": prompt_sistema}],
            stream=True 
        )
        
        for chunk in stream:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content
                
    except Exception as e:
        yield f"Erro na geração: {e}"
    # ---------------------------------------