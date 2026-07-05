def validate_api_response(response, expected_status, expected_fields=None, max_time=1.0):
    """Función helper para validar respuestas API
    con los 5 niveles.
    """

    # Nivel 1: Status
    assert response.status_code == expected_status

    # Nivel 2: headers
    if expected_status != 204:

        assert 'application/json' in response.headers.get('Content-Type', '')

        # Nivel 3-4: Estructura y contenido

        if expected_fields and response.text:
            body = response.json()
            assert expected_fields <= set(body.keys())

        # Nivel 5: Performance

    assert response.elapsed.total_seconds() < max_time
    return response.json() if response.text else {}

def assert_tiempo_respuesta(segundos, maximo):
    assert segundos < maximo, f"Excedió el tiempo: {segundos} > {maximo}s"