from unittest.mock import Mock
import pytest
from libpythonavatar.spam.main import EnviadorDeSpam
from libpythonavatar.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Renzo', email='renzo@gmail.com'),
            Usuario(nome='Carlos', email='carlos@gmail.com')
        ],
        [
            Usuario(nome='Renzo', email='renzo@gmail.com')
        ]
    ]
)
def test_qtd_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'renzo@gmail.com',
        'Teste de envio de email',
        'Confira os móddulos fantásticos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Renzo', email='renzo@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'carlos@gmail.com',
        'Teste de envio de email',
        'Confira os móddulos fantásticos'
    )
    enviador.enviar.assert_called_once_with(
        'carlos@gmail.com',
        'renzo@gmail.com',
        'Teste de envio de email',
        'Confira os móddulos fantásticos'
    )
