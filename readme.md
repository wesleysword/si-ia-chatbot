# Soluções Imobiliárias - Microsserviço de IA (ChatBot)

Este repositório contém o microsserviço de Inteligência Artificial desenvolvido em Python para atuar como o assistente conversacional da Soluções Imobiliárias. Ele se comunica exclusivamente com o backend (NestJS) e utiliza a API do Google Gemini para interpretar e responder aos leads.

---

## Tecnologias Utilizadas

* **Linguagem:** Python 3.11+
* **Framework Web:** FastAPI
* **Servidor ASGI:** Uvicorn
* **Inteligência Artificial:** Google Generative AI (Gemini 2.5 Flash)
* **Gerenciamento de Dados:** Pydantic
* **Infraestrutura:** Docker

---

## Pré-requisitos e Dependências

Para executar este projeto localmente, é necessário ter:

* [Python 3.11+](https://www.python.org/)
* [Docker Desktop](https://www.docker.com/products/docker-desktop) (Opcional, para execução via container)
* Uma chave de API válida do [Google AI Studio](https://aistudio.google.com/)

---

## Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto e adicione a sua chave de API do Gemini:

```env
GEMINI_API_KEY=sua_chave_secreta_aqui
```

---

## Passo a Passo para Execução Local

Você pode rodar a aplicação de duas formas: nativamente com Python ou isolada via Docker.

### Execução Nativa (Python + Venv)

**1. Clone o repositório:**
```bash
git clone https://github.com/SEU_USUARIO/si-ia-chatbot.git
cd si-ia-chatbot
```

**2. Crie e ative o ambiente virtual:**
* Windows: `python -m venv venv` e depois `venv\Scripts\activate`
* Linux/Mac: `python3 -m venv venv` e depois `source venv/bin/activate`

**3. Instale as dependências:**
```bash
pip install -r requirements.txt
```

**4. Inicie o servidor:**
```bash
uvicorn main:app --reload --port 8000
```

### Execução via Docker (Recomendado)

**1. Construa a imagem:**
```bash
docker build -t si-chatbot-ia .
```

**2. Rode o container:**
```bash
docker run -d -p 8000:8000 --env-file .env --name chatbot_container si-chatbot-ia
```

O serviço estará disponível em: `http://localhost:8000`. A documentação interativa (Swagger) pode ser acessada em `http://localhost:8000/docs`.

---

## Integração com a Aplicação

Este microsserviço não se comunica diretamente com o frontend. 
O fluxo de dados segue a arquitetura: `Frontend (NextJS) -> Backend (NestJS) -> Microsserviço de IA (FastAPI)`. O endpoint `/api/chat` recebe a nova mensagem do usuário junto com o histórico da conversa, processa o contexto imobiliário e devolve a resposta gerada pelo LLM.