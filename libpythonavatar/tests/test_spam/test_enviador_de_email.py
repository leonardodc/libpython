from pytest import mark
from libpythonavatar.spam.enviador_de_email import Enviador

def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

@mark.parametrize(
    'destinatario',
    ['leonardo_foz@hotmail.com', 'foo@bar.com.br']
)
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        'leonardodemeterko@gmail.com',
        'Curso Python',
        'Estudos aplicados em 2023'
    )
    assert destinatario in resultado