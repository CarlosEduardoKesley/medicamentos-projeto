import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from src.main import (
    adicionar_medicamento,
    editar_medicamento,
    deletar_medicamento,
    listar_medicamentos,
    buscar_clima,
)


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


# ── Integração com API de Clima ───────────────────────────────────────────────

def _criar_mock_cliente(temperatura: float):
    """Monta o mock do httpx.AsyncClient para o async with."""
    mock_resposta = MagicMock()
    mock_resposta.json.return_value = {
        "current": {"temperature_2m": temperatura, "weathercode": 0}
    }
    mock_resposta.raise_for_status = MagicMock()

    mock_client = AsyncMock()
    mock_client.get = AsyncMock(return_value=mock_resposta)

    mock_context = MagicMock()
    mock_context.__aenter__ = AsyncMock(return_value=mock_client)
    mock_context.__aexit__ = AsyncMock(return_value=False)

    return mock_context


@pytest.mark.asyncio
async def test_buscar_clima_calor():
    """Simula resposta da API com temperatura alta (≥ 35°C)."""
    with patch("httpx.AsyncClient", return_value=_criar_mock_cliente(37.0)):
        resultado = await buscar_clima()
    assert "37.0" in resultado
    assert "Hidrate" in resultado


@pytest.mark.asyncio
async def test_buscar_clima_frio():
    """Simula resposta da API com temperatura baixa (≤ 15°C)."""
    with patch("httpx.AsyncClient", return_value=_criar_mock_cliente(12.0)):
        resultado = await buscar_clima()
    assert "12.0" in resultado
    assert "Agasalhe" in resultado


@pytest.mark.asyncio
async def test_buscar_clima_agradavel():
    """Simula resposta da API com temperatura agradável."""
    with patch("httpx.AsyncClient", return_value=_criar_mock_cliente(22.0)):
        resultado = await buscar_clima()
    assert "22.0" in resultado
    assert "agradável" in resultado


@pytest.mark.asyncio
async def test_buscar_clima_falha_conexao():
    """Simula falha de conexão com a API."""
    mock_context = MagicMock()
    mock_context.__aenter__ = AsyncMock(side_effect=Exception("Timeout"))
    mock_context.__aexit__ = AsyncMock(return_value=False)

    with patch("httpx.AsyncClient", return_value=mock_context):
        resultado = await buscar_clima()
    assert "Não foi possível" in resultado
