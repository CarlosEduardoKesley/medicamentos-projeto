import os
import uuid
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

app = FastAPI()

DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
caminho_templates = os.path.join(DIRETORIO_ATUAL, "templates")
templates = Jinja2Templates(directory=caminho_templates)

# Base de dados em memória
medicamentos: list[dict] = [
    {"id": str(uuid.uuid4()), "nome": "Losartana 50mg", "horario": "08:00", "dose": "1 comprimido"},
    {"id": str(uuid.uuid4()), "nome": "Vitamina D", "horario": "12:00", "dose": "1 cápsula"},
]


# ---------- Funções de lógica (testáveis) ----------

def adicionar_medicamento(nome: str, horario: str, dose: str, lista: list) -> tuple:
    if not nome.strip() or not horario.strip():
        return False, "Os campos nome e horário são obrigatórios."
    lista.append({
        "id": str(uuid.uuid4()),
        "nome": nome.strip(),
        "horario": horario.strip(),
        "dose": dose.strip() or "Não informada",
    })
    return True, "Medicamento adicionado com sucesso."


def editar_medicamento(med_id: str, nome: str, horario: str, dose: str, lista: list) -> tuple:
    for med in lista:
        if med["id"] == med_id:
            if not nome.strip() or not horario.strip():
                return False, "Os campos nome e horário são obrigatórios."
            med["nome"] = nome.strip()
            med["horario"] = horario.strip()
            med["dose"] = dose.strip() or "Não informada"
            return True, "Medicamento atualizado com sucesso."
    return False, "Medicamento não encontrado."


def deletar_medicamento(med_id: str, lista: list) -> tuple:
    for i, med in enumerate(lista):
        if med["id"] == med_id:
            lista.pop(i)
            return True, "Medicamento removido."
    return False, "Medicamento não encontrado."


def listar_medicamentos(lista: list) -> str:
    if not lista:
        return "Nenhum medicamento cadastrado."
    return "\n".join(f"{m['horario']} - {m['nome']} ({m.get('dose', '')})" for m in lista)


# ---------- Rotas ----------

@app.get("/")
async def home(request: Request):
    ordenados = sorted(medicamentos, key=lambda m: m["horario"])
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"remedios": ordenados, "editando": None},
    )


@app.post("/adicionar")
async def rota_adicionar(
    nome: str = Form(...),
    horario: str = Form(...),
    dose: str = Form(""),
):
    adicionar_medicamento(nome, horario, dose, medicamentos)
    return RedirectResponse(url="/", status_code=303)


@app.get("/editar/{med_id}")
async def pagina_editar(request: Request, med_id: str):
    med = next((m for m in medicamentos if m["id"] == med_id), None)
    if not med:
        return RedirectResponse(url="/", status_code=303)
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "remedios": sorted(medicamentos, key=lambda m: m["horario"]),
            "editando": med,
        },
    )


@app.post("/editar/{med_id}")
async def rota_editar(
    med_id: str,
    nome: str = Form(...),
    horario: str = Form(...),
    dose: str = Form(""),
):
    editar_medicamento(med_id, nome, horario, dose, medicamentos)
    return RedirectResponse(url="/", status_code=303)


@app.post("/deletar/{med_id}")
async def rota_deletar(med_id: str):
    deletar_medicamento(med_id, medicamentos)
    return RedirectResponse(url="/", status_code=303)
