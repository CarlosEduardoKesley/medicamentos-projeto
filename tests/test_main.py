from src.main import adicionar_medicamento, editar_medicamento, deletar_medicamento, listar_medicamentos


# ── Adicionar ────────────────────────────────────────────────────────────────

def test_adicionar_caminho_feliz():
    lista = []
    sucesso, msg = adicionar_medicamento("Losartana", "08:00", "1 comprimido", lista)
    assert sucesso is True
    assert len(lista) == 1
    assert lista[0]["nome"] == "Losartana"
    assert lista[0]["dose"] == "1 comprimido"
    assert "id" in lista[0]


def test_adicionar_nome_vazio():
    lista = []
    sucesso, msg = adicionar_medicamento("", "08:00", "", lista)
    assert sucesso is False
    assert "obrigatórios" in msg
    assert len(lista) == 0


def test_adicionar_dose_padrao():
    lista = []
    adicionar_medicamento("Vitamina D", "12:00", "", lista)
    assert lista[0]["dose"] == "Não informada"


# ── Editar ───────────────────────────────────────────────────────────────────

def test_editar_caminho_feliz():
    lista = []
    adicionar_medicamento("Losartana", "08:00", "1 comp", lista)
    med_id = lista[0]["id"]

    sucesso, msg = editar_medicamento(med_id, "Losartana 50mg", "09:00", "2 comp", lista)
    assert sucesso is True
    assert lista[0]["nome"] == "Losartana 50mg"
    assert lista[0]["horario"] == "09:00"


def test_editar_id_inexistente():
    lista = []
    sucesso, msg = editar_medicamento("id-falso", "X", "10:00", "", lista)
    assert sucesso is False
    assert "não encontrado" in msg


# ── Deletar ──────────────────────────────────────────────────────────────────

def test_deletar_caminho_feliz():
    lista = []
    adicionar_medicamento("Vitamina C", "07:00", "1 comp", lista)
    med_id = lista[0]["id"]

    sucesso, msg = deletar_medicamento(med_id, lista)
    assert sucesso is True
    assert len(lista) == 0


def test_deletar_id_inexistente():
    lista = []
    sucesso, msg = deletar_medicamento("id-falso", lista)
    assert sucesso is False


# ── Listar ───────────────────────────────────────────────────────────────────

def test_listar_vazio():
    assert listar_medicamentos([]) == "Nenhum medicamento cadastrado."


def test_listar_com_itens():
    lista = []
    adicionar_medicamento("Losartana", "08:00", "1 comp", lista)
    resultado = listar_medicamentos(lista)
    assert "Losartana" in resultado
    assert "08:00" in resultado
