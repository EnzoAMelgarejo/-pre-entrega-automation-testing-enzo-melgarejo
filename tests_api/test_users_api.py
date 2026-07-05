import requests
import pytest
import pytest_check as check
from utils.logger_config import logger

API_KEY = 'free_user_3FumSZcGRMbgkmwRjVIvwOgg4ZU'
URL = 'https://reqres.in/api/users?page=1'

@pytest.mark.api
def test_get_users():
    headers = {'x-api-key': API_KEY}
    logger.info(f"Enviando GET a {URL}")
    r = requests.get(URL, headers=headers)
    check.equal(r.status_code, 200, "El status no es 200")

    data = r.json()
    check.equal(data['page'], 1, "La página no es 1")

    usuario = data['data'][0]
    check.is_true({'id', 'email', 'first_name', 'last_name'} <= set(usuario.keys()),
                  "Faltan campos esperados en el usuario")
    check.is_true(usuario['avatar'].endswith('.jpg'), "El avatar no termina en .jpg")
    logger.info(f"Validaciones completas para usuario id={usuario.get('id')}")