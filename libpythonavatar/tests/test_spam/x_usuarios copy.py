import pytest
from libpythonavatar.spam.db import Conexao
from libpythonavatar.spam.modelos import Usuario


# ! Esse arquivo foi antes de redução de código

@pytest.fixture
def conexao():
    return Conexao()

@pytest.fixture
def sessao(conexao):
    sessao_obj = conexao.gerar_sessao()
    return sessao_obj
    
def test_salvar_usuario(conexao, sessao):
    usuario = Usuario(nome='Renzo')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()

def test_listar_usuarios(conexao, sessao):
    usuarios = [Usuario(nome='Renzo'), Usuario(nome='Carlos')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()
