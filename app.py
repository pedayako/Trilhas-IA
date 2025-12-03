import streamlit as st
import time
import seguranca      
import banco_dados    
import ingestao       
import resposta_ia    

st.set_page_config(page_title="Secure RAG", page_icon="🛡️")
st.title("🛡️ Sistema de Chat Corporativo")

with st.sidebar:
    if st.button("🔄 Atualizar Banco"):
        ingestao.executar_ingestao()
        st.success("Concluído!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Digite sua pergunta..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.status("🔍 Analisando segurança...", expanded=True) as status:
            
            # [MISSÃO 7]: Sentinel (Anti-Injection)
            # Chame a função seguranca.analisar_risco_injecao(prompt)
            # Se retornar False, exiba st.error("...") e use st.stop()
            
            # if not seguranca.analisar_risco_injecao(prompt):
            #     st.error("BLOQUEADO PELO SENTINEL")
            #     st.stop()
            
            st.write("✅ Sentinel: OK")

            # [MISSÃO 8]: Compliance (Intenção)
            # Chame seguranca.classificar_intencao(prompt)
            # Se o retorno for igual a "BLOQUEADO", pare o app.
            
            # ... código aqui ...
            
            st.write("✅ Compliance: OK")
            
            # [MISSÃO 9]: RAG (Busca)
            # Chame banco_dados.buscar_contexto(prompt) e guarde na variavel contexto
            
            contexto = banco_dados.buscar_contexto(prompt)
            st.write("📚 Documentos consultados.")
            
            status.update(label="✅ Verificado!", state="complete", expanded=False)

        # [MISSÃO 10]: Exibir Resposta
        fluxo = resposta_ia.gerar_resposta_final_stream(prompt, contexto)
        st.write_stream(fluxo)