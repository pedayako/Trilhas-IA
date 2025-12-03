import ingestao
import banco_dados
import seguranca
import resposta_ia  # <--- 1. IMPORTANTE: Adicionar este import

def iniciar_chat():
    print("\n🔒 Terminal Seguro Banco Horizon v3.0 (Modular)")
    
    while True:
        pergunta = input("\nFuncionário(a): ")
        if pergunta.lower() in ["sair", "exit"]: break

        # 1. CAMADA SENTINELA (Anti-Injection)
        # O 'not' aqui é essencial (Bloqueia se NÃO for seguro)
        if not seguranca.analisar_risco_injecao(pergunta):
            print("🚫 BLOQUEIO: Tentativa de manipulação detectada.")
            continue

        # 2. CAMADA COMPLIANCE (Few-Shot)
        classificacao = seguranca.classificar_intencao(pergunta)
        if "BLOQUEADO" in classificacao:
            print("🚫 BLOQUEIO: Tema não permitido pela política de segurança.")
            continue

        # 3. BUSCA E RESPOSTA
        print("✅ Processando...")
        contexto = banco_dados.buscar_contexto(pergunta)
        
        # --- MUDANÇA AQUI: Usando o resposta_ia.py no Terminal ---
        print("🤖 Horizon AI: ", end="", flush=True)
        
        # Chamamos o gerador (stream)
        fluxo = resposta_ia.gerar_resposta_final_stream(pergunta, contexto)
        
        # Loop para imprimir pedacinho por pedacinho no terminal
        for texto in fluxo:
            print(texto, end="", flush=True) # flush=True força o texto a aparecer na hora
        print("\n") # Pula linha no final

if __name__ == "__main__":
    while True:
        print("\n=== MENU ===")
        print("1. Ingestão de Documentos")
        print("2. Chat Seguro")
        print("3. Sair")
        
        op = input("Opção: ")
        if op == "1": ingestao.executar_ingestao()
        elif op == "2": iniciar_chat()
        elif op == "3": break