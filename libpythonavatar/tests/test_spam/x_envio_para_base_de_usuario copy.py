import pytest
from libpythonavatar.spam.enviador_de_email import Enviador
from libpythonavatar.spam.main import EnviadorDeSpam
from libpythonavatar.spam.modelos import Usuario

# ! Antes de usar a classe Mock do Unitest


class EnviadorMock(Enviador):
    def __init__(self):
        super().__init__()
        self.qtd_de_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_de_email_enviados += 1


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
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'renzo@gmail.com',
        'Teste de envio de email',
        'Confira os móddulos fantásticos'
    )
    assert len(usuarios) == enviador.qtd_de_email_enviados


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Renzo', email='renzo@gmail.com')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'carlos@gmail.com',
        'Teste de envio de email',
        'Confira os móddulos fantásticos'
    )
    assert enviador.parametros_de_envio == (
        'carlos@gmail.com',
        'renzo@gmail.com',
        'Teste de envio de email',
        'Confira os móddulos fantásticos'
    )
