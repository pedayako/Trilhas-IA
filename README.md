# 📚 Trilhas IA — Desenvolvimento de Modelos Aplicados a Chatbots

> **Este repositório é material didático.**
> Ele foi pensado para alunos que estão aprendendo **LLMs, Prompt Engineering e RAG**, com foco em **entender conceitos na prática**, sem pular etapas.

---

## 🎯 Objetivo da Trilha

Ao final desta trilha, você será capaz de:

* Entender **como LLMs funcionam de verdade** (e suas limitações)
* Criar **prompts melhores e mais confiáveis**
* Construir um chatbot que **conversa com seus próprios dados (RAG)**
* Compreender por que **arquitetura importa** em projetos de IA
* Evoluir um código **monolítico → modular**, de forma consciente

Esta trilha não é sobre decorar ferramentas — é sobre **raciocinar como quem constrói sistemas de IA**.

---

## 🧭 Como este Repositório Funciona (IMPORTANTE)

Este repositório **usa branches como trilhas de aprendizado**.

👉 **Você NÃO vai encontrar tudo ao mesmo tempo.**
Cada branch representa uma fase do aprendizado.

### 🔹 Branch `baseline` (comece por aqui)

* Código **monolítico**
* Tudo em poucos arquivos
* Ideal para **entender o fluxo completo** sem abstrações
* Onde estão os códigos dos hands-on

👉 É aqui que você **aprende primeiro**.

### 🔹 Branch `architecture/modular`

* Código **organizado em módulos**
* Separação clara de responsabilidades
* Estrutura mais próxima do **mundo real / produção**

👉 É aqui que você aprende **como evoluir um projeto**.

---

## 🚦 Qual branch eu devo usar?

| Situação                          | Branch                 |
| --------------------------------- | ---------------------- |
| Primeiro contato com o projeto    | `baseline`             |
| Executar os hands-on              | `baseline`             |
| Estudar arquitetura e organização | `architecture/modular` |
| Comparar monolito vs modular      | As duas                |

---

## 🧠 O que você vai aprender

### 1️⃣ Fundamentos de LLMs

* O que é (e o que não é) um LLM
* Tokenização
* Embeddings
* Transformers e Self-Attention
* Limitações:

  * Alucinações
  * Sensibilidade a prompts
  * Desatualização
  * Riscos de segurança

---

### 2️⃣ Engenharia de Prompt

Você vai aprender que **prompt é código**.

Técnicas usadas:

* Zero-shot
* Few-shot
* Chain-of-Thought (CoT)
* Role Playing
* Templates reutilizáveis

Boas práticas trabalhadas:

* Ser explícito
* Estruturar instruções
* Definir persona
* Limitar escopo
* Controlar formato da saída

---

### 3️⃣ RAG — Converse com seus Dados

Aqui o modelo ganha **memória externa**.

Você aprende:

* Por que LLMs alucinam
* Como o RAG reduz esse problema
* O papel dos embeddings
* Busca por similaridade
* Montagem do prompt com contexto

Fluxo simplificado:

1. Pergunta do usuário
2. Embedding da pergunta
3. Busca no banco vetorial
4. Montagem do prompt com contexto
5. Resposta fundamentada

---

### 4️⃣ Segurança em Sistemas com LLMs

Porque **LLM sem proteção é risco**.

Você verá na prática:

* Prompt Injection
* Guardrails
* Sanitização de entrada
* Validação de permissões
* Boas práticas para produção

---

## 🧪 Hands-On (Prática)

### 🔹 Hands-On 1 — Prompt Engineering

Objetivo: perceber como **a forma da pergunta muda totalmente a resposta**.

Branch:

```bash
git checkout baseline
```

Execução:

```bash
pip install groq python-dotenv
python prompt_eng.py
```

---

### 🔹 Hands-On 2 — RAG

Objetivo: construir um chatbot que responde **usando seus próprios documentos**.

Branch:

```bash
git checkout baseline
```

Execução:

```bash
pip install chromadb pypdf python-docx streamlit
python rag.py
```

## 🚀 Como aproveitar melhor a trilha

✔ Execute o código
✔ Leia os comentários
✔ Quebre o projeto sem medo
✔ Compare as branches
✔ Teste variações de prompt

---

## 👨‍🏫 Sobre o Instrutor
Entre em contato comigo! Vou ficar feliz em poder te ajudar :)

📧 [pedro.franca@nca.ufma.br](mailto:pedro.franca@nca.ufma.br)
🐙 Linkedin: pedrof-ia

---

## ✅ Mensagem Final

Este repositório é um **laboratório de aprendizado**.

Se algo não funcionar de primeira, ótimo — é assim que se aprende.

Boa trilha 🚀
