# SI - Microserviço de Inteligência Artificial

Este repositório contém o microserviço dedicado ao processamento de Inteligência Artificial do CRM. Ele opera separadamente do servidor principal, garantindo uma arquitetura escalável (Microservices). Utiliza a API do Google Gemini para atuar como a "SIA", assistente virtual do sistema.

## Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Framework Web:** FastAPI (Alta performance para APIs REST)
* **Servidor ASGI:** Uvicorn
* **Inteligência Artificial:** Google Generative AI (Gemini 2.5 Flash)
* **Validação de Dados:** Pydantic

## Funcionalidades

* **Endpoint `/api/chat`:** Recebe requisições POST contendo a pergunta do usuário e o **contexto em tempo real do banco de dados** (injetado via NestJS).
* **Prompt Engineering Dinâmico:** Constrói um contexto instrucional dinâmico, forçando a IA a analisar exclusivamente os dados imobiliários enviados, gerando respostas altamente precisas e profissionais.
* **CORS Integrado:** Configurado com middlewares de segurança para aceitar requisições do ecossistema local e de produção.

## Como Executar o Microserviço

1.  **Clone o repositório e acesse a pasta:**
    ```bash
    git clone <url-deste-repositorio>
    cd si-ia-chatbot
    ```

2.  **Instale as dependências:**
    ```bash
    python -m pip install fastapi uvicorn google-generativeai python-dotenv pydantic
    ```

3.  **Configuração de Variáveis de Ambiente:**
    Crie um arquivo `.env` na raiz do projeto e adicione sua chave de API do Google Gemini:
    ```env
    GEMINI_API_KEY="sua_chave_aqui"
    ```

4.  **Inicie o servidor FastAPI:**
    ```bash
    python -m uvicorn main:app --reload
    ```

O microserviço de IA iniciará e ficará escutando requisições na porta `http://127.0.0.1:8000`.

---
*Desenvolvido por Wesley - Desenvolvedor Full Stack*