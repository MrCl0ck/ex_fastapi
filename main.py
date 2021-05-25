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
@app.get("/usuarios/{id_usuario}")
def get_id(id_usuario: int):
    for usuario in base_de_dados:
        if(usuario.id == id_usuario):
            return usuario
        
    return "Usuário não encontrado!"

#Rota Inserir
@app.post("/usuarios")
def insert_user(usuario: Usuario):
    return base_de_dados.append(usuario)

#Desafio: criar rotas para alterar, deletar...
#Desafio2: criar validação de dados, tanto para id quanto para 'email'. É importante que no bd não tenha dados repetidos.