# Proyecto Final - Automation Testing con POM
**Autor:** Tu Melgerjo Enzo
**Repositorio:** https://github.com/EnzoAMelgarejo/-pre-entrega-automation-testing-enzo-melgarejo.git

## Propósito del proyecto
Este proyecto automatiza pruebas funcionales sobre SauceDemo utilizando Selenium WebDriver y Pytest, implementando el patrón de diseño Page Object Model (POM).

Las pruebas cubren:
- Login de usuario (exitoso y fallido)
- Navegación del catálogo
- Interacción con el carrito de compras
- Flujo completo end-to-end

---
## Tecnologías utilizadas
- Python
- Pytest
- Selenium WebDriver
- Git / GitHub

---
## Instalación de dependencias
```bash
pip install -r requirements.txt
```

---
## Ejecución de pruebas
Todas las pruebas:
```bash
pytest -v
```
Solo tests de regresión:
```bash
pytest -m regression -v
```
Solo tests de smoke:
```bash
pytest -m smoke -v
```
Generar reporte HTML:
```bash
pytest --html=reporte_pom.html --self-contained-html -v
```