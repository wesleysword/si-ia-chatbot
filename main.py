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
        
        contexto_imobiliario = (
            "INSTRUÇÃO DE SISTEMA: Você é um assistente virtual da 'SI - Soluções Imobiliárias'. Seu nome é SIA"
            "Seja sempre educado e focado em encontrar o melhor imóvel para o cliente, de forma que sempre permaneça neste mesmo contexto. "
            "Baseie-se no histórico da conversa.\n\n"
        )
        
        response = chat_session.send_message(contexto_imobiliario + request.message)
        
        return {"reply": response.text}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao processar a mensagem: {str(e)}")

@app.get("/")
async def root():
    return {"status": "Microsserviço de IA operando com sucesso"}