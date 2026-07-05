import requests
import datetime
import pytest
from faker import Faker
from utils.logger_config import logger

CREATE_URL = 'https://reqres.in/api/users'
API_KEY = 'free_user_3FumSZcGRMbgkmwRjVIvwOgg4ZU'
fake = Faker()
CASOS_USUARIOS = [(fake.name(), fake.job()) for _ in range(3)]

@pytest.mark.api
@pytest.mark.parametrize("name, job", CASOS_USUARIOS)
def test_post_user(name, job):
    headers = {'x-api-key': API_KEY}
    payload = {'name': name, 'job': job}
    logger.info(f"Creando usuario name={name}, job={job}")
    r = requests.post(CREATE_URL, json=payload, headers=headers)
    assert r.status_code == 201
    new_user = r.json()
    anio_actual = str(datetime.datetime.now().year)
    assert anio_actual in new_user['createdAt']
    logger.info(f"Usuario creado correctamente con id={new_user['id']}, createdAt={new_user['createdAt']}")