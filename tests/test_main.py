from src.main import adicionar_medicamento, listar_medicamentos

def test_adicionar_medicamento_caminho_feliz():
    # 1. Caminho Feliz
    lista = []
    sucesso, msg = adicionar_medicamento("Losartana", "08:00", lista)
    
    assert sucesso is True
    assert len(lista) == 1
    assert lista[0]["nome"] == "Losartana"

def test_adicionar_medicamento_invalido():
    # 2. Entrada Inválida (nome vazio)
    lista = []
    sucesso, msg = adicionar_medicamento("", "12:00", lista)
    
    assert sucesso is False
    assert "obrigatórios" in msg
    assert len(lista) == 0

def test_listar_medicamentos_vazio():
    # 3. Caso Limite (listar sem nada cadastrado)
    lista = []
    resultado = listar_medicamentos(lista)
    
    assert resultado == "Nenhum medicamento cadastrado."