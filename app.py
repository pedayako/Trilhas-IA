import streamlit as st
import time
import seguranca      # Para os Guardrails
import banco_dados    # Para o RAG
import ingestao       # Para ler arquivos
import resposta_ia    # <--- NOVO IMPORT AQUI

# Configuração da Página
st.set_page_config(page_title="Banco Horizon Secure Chat", page_icon="🛡️")
st.title("🛡️ Guardião Horizon v3.0")

# --- SIDEBAR ---
with st.sidebar:
    st.header("⚙️ Painel Admin")
    if st.button("🔄 Atualizar Conhecimento (Ingestão)"):
        with st.spinner("Lendo documentos..."):
            ingestao.executar_ingestao()
        st.success("Banco de dados atualizado!")
    
    st.info("Nível de Segurança: ALTO (3)")
    st.markdown("---")
    st.caption("Developed for Horizon Bank Workshop")

# --- HISTÓRICO ---
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- FLUXO PRINCIPAL ---
if prompt := st.chat_input("Digite sua dúvida operacional..."):
    
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        
        # --- VERIFICAÇÃO DE SEGURANÇA ---
        with st.status("🔍 Analisando segurança...", expanded=True) as status:
            
            # 1. Sentinel
            st.write("🤖 Consultando AI Sentinel (Anti-Injection)...")
            time.sleep(0.5)
            if not seguranca.analisar_risco_injecao(prompt):
                status.update(label="🚨 Ameaça Detectada!", state="error")
                st.error("BLOQUEIO: Tentativa de manipulação de prompt identificada.")
                st.stop()
            st.write("✅ Input Seguro.")
            
            # 2. Compliance
            st.write("⚖️ Verificando Compliance (Política Nível 3)...")
            intencao = seguranca.classificar_intencao(prompt)
            if "BLOQUEADO" in intencao:
                status.update(label="🚫 Acesso Negado", state="error")
                st.error("BLOQUEIO: O tema solicitado viola as políticas de confidencialidade.")
                st.stop()
            st.write("✅ Tema Permitido.")
            
            # 3. Busca no Banco
            st.write("📚 Buscando documentos internos...")
            contexto = banco_dados.buscar_contexto(prompt)
            status.update(label="✅ Verificação Concluída. Gerando resposta...", state="complete", expanded=False)

        # --- GERAÇÃO FINAL (USANDO O NOVO ARQUIVO) ---
        # Chamamos a função do arquivo resposta_ia.py
        fluxo_resposta = resposta_ia.gerar_resposta_final_stream(prompt, contexto)
        
        # Escreve na tela
        resposta_completa = st.write_stream(fluxo_resposta)
        
        # Salva no histórico
        st.session_state.messages.append({"role": "assistant", "content": resposta_completa})