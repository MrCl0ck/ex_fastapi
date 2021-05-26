import string
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

#Validação de dados
def validar(email: str):
    email = email.lower()
    for usuario in base_de_dados:
        if(usuario.email == email):
            return "E-mail já existente!"
            
    return "Usuário disponível!"

#Rota Get All
@app.get("/usuarios")
def get_all():
    return base_de_dados

@app.get("/get")
def tamanho(): #retorna o tamanho do banco de dados
    return len(base_de_dados)

#Rota Get User
@app.get("/usuarios/{email}")
def get_user(email: str):
    for usuario in base_de_dados:
        if(usuario.email == email):
            return usuario
        
    return "Usuário não encontrado!"

#Rota Inserir
@app.post("/usuarios")
def insert_user(email: str, senha: str):
    val = validar(email)#atribui à variável o retorno da função validar, que pode ser um "usuário disponível" OU  'usuário não disponível'
    if(val == "Usuário disponível!"): #Se o usuário estiver disponível ele insere no banco e retorna mensagem de sucesso
        base_de_dados.append(Usuario(id=tamanho()+1, email=email.lower(), senha=senha)) #insere sempre um novo usuário na última posição + 1
        return "Usuário inserido com sucesso!"

    return val

#Rota Alterar
@app.put("/usuarios/{dados}")
def alter_user(email_antigo: str, email_novo: str, senha_nova: str):
    alterar = get_user(email_antigo)#atribui à variável o retorno da função get_user, que pode ser um usuário OU  'Email já existente!'

    if(alterar == "Usuário não encontrado!"):#Retorno em que o usuário não é encontrado
        return alterar;

    base_de_dados.remove(alterar) #remove o usuário antigo, pois está disponível.

    val = validar(email_novo)#atribui à variável o retorno da função validar, que pode ser um "usuário disponível" OU  'Email já existente!'

    if(val == "Usuário disponível!"): #Se o usuário estiver disponível ele insere no banco e retorna mensagem de sucesso
        base_de_dados.append(Usuario(id=alterar.id, email=email_novo.lower(), senha=senha_nova)) #adiciona ao banco de dados o usuário
        return "Usuário alterado com sucesso!"
    else:
        base_de_dados.append(alterar)#readiciona ao banco de dados o usuário que foi removido
        return "Usuário alterado com sucesso!"

    
@app.delete("/usuarios/{email}")
def delete_user(email: str): #deleta o usuário por email.
    remover = get_user(email) #atribui à variável o retorno da função get_user, que pode ser um usuário OU  'usuário não encontrado'

    if(remover == "Usuário não encontrado!"): #Retorno em que o usuário não é encontrado
        return remover;

    base_de_dados.remove(remover) #remove o usuário do banco de dados

    index = 1
    for user in base_de_dados: #atualiza os ids dos usuários do banco de dados
        user.id = index
        index += 1

    return "Usuário deletado com sucesso!"

#Desafio: criar rotas para alterar, deletar... ok
#Desafio2: criar validação de dados, tanto para id quanto para 'email'. É importante que no bd não tenha dados repetidos.