import pytest
from libpythonavatar.spam.enviador_de_email import Enviador, EmailInvalido

def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'remetente',
    ['leonardo_foz@hotmail.com', 'foo@bar.com.br']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'leonardodemeterko@gmail.com',
        'Curso Python',
        'Estudos aplicados em 2023'
    )
    assert remetente in resultado

@pytest.mark.parametrize(
    'remetente',
    ['', 'renzo']
)
def test_remetente_Invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'leonardodemeterko@gmail.com',
            'Curso Python',
            'Estudos aplicados em 2023'
        )
    