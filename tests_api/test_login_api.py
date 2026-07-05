import pytest
import requests
from utils.datos import leer_login_json
from utils.logger_config import logger

API_KEY = 'free_user_3FumSZcGRMbgkmwRjVIvwOgg4ZU'
CASOS_LOGIN = leer_login_json('datos/login.json')
LOGIN_URL = 'https://reqres.in/api/login'

@pytest.mark.api
@pytest.mark.parametrize("usuario, clave, debe_funcionar, descripcion", CASOS_LOGIN)
def test_login_succesfull(usuario, clave, debe_funcionar, descripcion):
    headers = {'x-api-key': API_KEY}
    creds = {"email": usuario, "password": clave}
    logger.info(f"Probando login '{descripcion}' con usuario={usuario} (se espera éxito={debe_funcionar})")
    resp = requests.post(LOGIN_URL, json=creds, headers=headers)

    if debe_funcionar:
        assert resp.status_code == 200
        assert 'token' in resp.json()
        logger.info(f"Login exitoso para {usuario}, token recibido")
    else:
        assert resp.status_code == 400
        logger.info(f"Login fallido como se esperaba para {usuario} (status 400)")