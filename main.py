import os
import google.generativeai as genai
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = FastAPI(title="SI - IA ChatBot")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = genai.GenerativeModel('gemini-2.5-flash')

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    message: str
    history: List[Message] = []
    crm_context: str = ""

@app.post("/api/chat")
async def chat_endpoint(request: ChatRequest):
    try:
        gemini_history = []
        for msg in request.history:
            role = "model" if msg.role == "model" else "user"
            gemini_history.append({
                "role": role,
                "parts": [msg.content]
            })

        chat_session = model.start_chat(history=gemini_history)
        
        contexto_imobiliario = f"""
        INSTRUÇÃO DE SISTEMA: Você é a 'SIA', assistente virtual da 'SI - Soluções Imobiliárias'.
        Seja educada, profissional e ajude o corretor analisando os dados reais dos clientes abaixo.
        Se a pergunta não tiver relação com os clientes, responda normalmente sobre o mercado imobiliário.
        
        DADOS REAIS DOS CLIENTES NO CRM HOJE:
        {request.crm_context}
        
        PERGUNTA DO CORRETOR:
        """
        
        response = chat_session.send_message(contexto_imobiliario + request.message)
        
        return {"reply": response.text}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao processar a mensagem: {str(e)}")

@app.get("/")
async def root():
    return {"status": "Microsserviço de IA operando com sucesso"}