from groq import Groq
from config import GROQ_API_KEY, MODELO_IA

client_groq = Groq(api_key=GROQ_API_KEY)

def analisar_risco_injecao(texto_usuario):
    """
    Analisa se o prompt é malicioso (Jailbreak/Injection).
    """
    print(f"  [Sentinel] Analisando...")
    
    # [MISSÃO 1]: Defina a PALAVRA-CHAVE para ataques.
    PALAVRA_CHAVE_BLOQUEIO = "???" 
    
    # [MISSÃO 2]: Escreva o Prompt do Sentinel.
    # Instrua a IA a responder APENAS a sua PALAVRA_CHAVE_BLOQUEIO se for ataque.
    prompt = f"""
    <INSTRUCAO>
    
    <INPUT>
    {texto_usuario}
    </INPUT>
    """

    # --- ÁREA TÉCNICA (NÃO MEXER) ---
    try:
        resposta = client_groq.chat.completions.create(
            model=MODELO_IA,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0
        )
        conteudo = resposta.choices[0].message.content.strip().upper()
    except Exception as e:
        print(f"Erro na API: {e}")
        return True # Libera em caso de erro técnico
    # --------------------------------
        
    # [MISSÃO 3]: Valide a resposta da IA.
    # Se a PALAVRA_CHAVE_BLOQUEIO apareceu no 'conteudo', retorne False (Perigo).
    # Caso contrário, retorne True (Seguro).
    
    # if ??? in conteudo:
    #     return False
    
    return True # (Placeholder - ajuste a lógica acima)


def classificar_intencao(texto_usuario):
    """
    Classifica se o tema é PERMITIDO ou BLOQUEADO.
    """
    
    # [MISSÃO 4]: Escreva o Prompt de Compliance (Few-Shot).
    prompt = f"""
    Classifique a intenção do usuário.
    
    Input: "{texto_usuario}"
    Classificação:
    """

    # --- ÁREA TÉCNICA (NÃO MEXER) ---
    try:
        resposta = client_groq.chat.completions.create(
            model=MODELO_IA,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0
        )
        return resposta.choices[0].message.content.strip().upper()
    except Exception as e:
        return "PERMITIDO"
    # --------------------------------