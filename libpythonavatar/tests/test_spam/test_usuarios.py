from libpythonavatar.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Renzo', email='renzo@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [
        Usuario(nome='Renzo', email='renzo@gmail.com'),
        Usuario(nome='Carlos', email='carlos@gmail.com')
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
