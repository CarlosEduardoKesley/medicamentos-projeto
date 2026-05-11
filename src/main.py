import os
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

app = FastAPI()

# Isso garante que o Python ache a pasta templates não importa onde o terminal esteja!
DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
caminho_templates = os.path.join(DIRETORIO_ATUAL, "templates")

templates = Jinja2Templates(directory=caminho_templates)

# Sua "base de dados" na memória
medicamentos = [
    {"nome": "Losartana 50mg", "horario": "08:00"},
    {"nome": "Vitamina D", "horario": "12:00"}
]

@app.get("/")
async def home(request: Request):
    alerta_clima = "Sistema online! Caminho das pastas corrigido com sucesso."
    return templates.TemplateResponse(
        request=request,
        name="index.html", 
        context={"request": request, "remedios": medicamentos, "alerta": alerta_clima}
    )

@app.post("/adicionar")
async def adicionar_remedio(nome: str = Form(...), horario: str = Form(...)):
    medicamentos.append({"nome": nome, "horario": horario})
    return RedirectResponse(url="/", status_code=303)