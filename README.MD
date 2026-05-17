# Proyecto Final - Automation Testing

## Propósito del proyecto

Este proyecto tiene como objetivo automatizar pruebas funcionales sobre la página SauceDemo utilizando Selenium WebDriver y Pytest.

Las pruebas automatizadas verifican funcionalidades principales como:
- Login de usuario
- Navegación del catálogo
- Validación de productos
- Interacción con el carrito de compras

---

## Tecnologías utilizadas

- Python
- Pytest
- Selenium WebDriver
- Git
- GitHub

---

## Instalación de dependencias

Instalar las dependencias necesarias con:

```bash
pip install selenium
pip install pytest
pip install pytest-html
```

---

## Ejecución de pruebas

Ejecutar todas las pruebas:

```bash
pytest -v
```

Generar reporte HTML:

```bash
pytest -v --html=reporte.html
```