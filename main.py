from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Rota raiz
@app.get("/")
def raiz():
    return {"Olá":"Mundo"}

#Criar model
class Usuario(BaseModel):
    id: int
    email: str
    senha: str

#Criar base de dados
base_de_dados = [
    Usuario(id=1, email="teste@teste.com.br", senha="teste543"),
    Usuario(id=2, email="file@file.com.br", senha="file123")
]

#Rota Get All
@app.get("/usuarios")
def get_all():
    return base_de_dados

#Rota Get Id
