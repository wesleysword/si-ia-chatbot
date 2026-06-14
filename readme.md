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

## Executando com Docker (Recomendado)

1.  **Clone o repositório:**
    ```bash
    git clone <url-deste-repositorio>
    cd si-ia-chatbot
    ```

2.  **Configuração da Chave da API:**
    Crie um arquivo `.env` na raiz do projeto e adicione sua chave do Google Gemini:
    ```env
    GEMINI_API_KEY="sua_chave_aqui"
    ```

3.  **Construa e rode o container:**
    ```bash
    docker build -t si-ia-chatbot .
    docker run -d -p 8000:8000 --env-file .env --name chatbot si-ia-chatbot
    ```

O microserviço ficará disponível na porta `http://localhost:8000`.

## Executando Localmente (Sem Docker)

1.  **Clone o repositório:**
    ```bash
    git clone <url-deste-repositorio>
    cd si-ia-chatbot
    ```

2.  **Configuração da Chave da API:**
    Crie um arquivo `.env` na raiz do projeto e adicione sua chave do Google Gemini:
    ```env
    GEMINI_API_KEY="sua_chave_aqui"
    ```
3. Instale as bibliotecas: `pip install fastapi uvicorn google-generativeai python-dotenv pydantic`
4. Inicie o servidor: `python -m uvicorn main:app --reload`

---
*Desenvolvido por Wesley - Desenvolvedor Full Stack*