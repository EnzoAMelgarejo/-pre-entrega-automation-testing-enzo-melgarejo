import csv
import pathlib
import json

def leer_csv_login(ruta_archivo):
    """
    Lee un archivo CSV y devuelve una lista de tuplas
    para usar en parametrización de pytest
    """

    datos = []
    URI = pathlib.Path(ruta_archivo)
    with open(URI, newline='', encoding='utf-8') as f:
        br = csv.DictReader(f)
        for line in br:
            # Convertir string 'True'/'False' a booleano
            debe_funcionar = line['debe_funcionar'].lower() == 'true'
            datos.append((line['usuario'], line['clave'],
            debe_funcionar, line['descripcion']))
    return datos

def leer_json(ruta_archivo):
    """
    Lee un archuvo JSON con
    información de productos
    """

    with open(ruta_archivo, 'r', encoding='utf-8') as f:
        br = json.load(f)
        
        #Extraer solo los nombres para parametrización
        nombres = [line['nombre'] for line in br]
        return nombres

def leer_login_json(ruta_archivo):
    """
    Lee un archuvo JSON con
    información de productos
    """

    with open(ruta_archivo, 'r', encoding='utf-8') as f:
        br = json.load(f)
        
        #Extraer solo los nombres para parametrización
        datos = [(line['usuario'], line['clave'], line['debe_funcionar'], line['descripcion']) for line in br]
        return datos


# Ejemplo de uso
if __name__ == "__main__":
    casos = leer_csv_login('datos/login.csv')
    print(casos)
    # Resultado: [('standard_user', 'secret_sauce', 'True), ...]

    productos = leer_json('datos/productos.json')
    print(productos)
    #Resultado: ['Sauce Labs Backpack', 'Sauce Labs Bike Light', ...]