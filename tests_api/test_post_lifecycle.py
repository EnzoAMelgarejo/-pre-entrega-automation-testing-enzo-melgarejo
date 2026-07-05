import requests
import time
import pytest
from faker import Faker
from utils.api_utils import validate_api_response, assert_tiempo_respuesta
from utils.logger_config import logger

fake = Faker()
BASE_URL = 'https://jsonplaceholder.typicode.com/posts'
TIEMPO_MAXIMO_FLUJO = 5

@pytest.mark.api
@pytest.mark.e2e
@pytest.mark.flaky(reruns=2, reruns_delay=2)
def test_post_lifecycle():
    session = requests.Session()
    inicio = time.time()

    # 1. CREATE
    payload_create = {
        'title': fake.sentence(),
        'body': fake.paragraph(),
        'id': fake.random_int(min=1, max=10)
    }
    logger.info(f"Enviando POST a {BASE_URL} con payload: {payload_create}")
    r_create = session.post(BASE_URL, json=payload_create)
    data_create = validate_api_response(
        r_create,
        expected_status=201,
        expected_fields={'id', 'title', 'body'},
        max_time=3.0
    )
    assert isinstance(data_create['id'], int)
    post_id = data_create['id']
    logger.info(f"Post creado con id={post_id}")

    # 2. UPDATE (PATCH)
    payload_update = {'title': 'Titulo actualizado por QA'}
    logger.info(f"Enviando PATCH a {BASE_URL}/{post_id} con payload: {payload_update}")
    r_update = session.patch(f'{BASE_URL}/{post_id}', json=payload_update)
    data_update = validate_api_response(
        r_update,
        expected_status=200,
        expected_fields={'title'},
        max_time=3.0
    )
    assert data_update['title'] == 'Titulo actualizado por QA'
    logger.info("Titulo actualizado correctamente")

    # 3. DELETE
    logger.info(f"Enviando DELETE a {BASE_URL}/{post_id}")
    r_delete = session.delete(f'{BASE_URL}/{post_id}')
    validate_api_response(r_delete, expected_status=200, max_time=3.0)
    logger.info(f"Post {post_id} eliminado correctamente")

    fin = time.time()
    assert_tiempo_respuesta(fin - inicio, TIEMPO_MAXIMO_FLUJO)
    logger.info(f"Flujo completo en {fin - inicio:.2f}s")