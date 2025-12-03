import ingestao
import banco_dados
import seguranca

def iniciar_chat():
    print("\n🔒 Terminal Seguro Banco Horizon v3.0 (Modular)")
    
    while True:
        pergunta = input("\nFuncionário(a): ")
        if pergunta.lower() in ["sair", "exit"]: break

        # 1. CAMADA SENTINELA (Anti-Injection)
        if seguranca.analisar_risco_injecao(pergunta):
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
        seguranca.gerar_resposta_segura(pergunta, contexto)

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