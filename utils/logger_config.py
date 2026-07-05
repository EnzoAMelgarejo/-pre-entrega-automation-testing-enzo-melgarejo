import logging
import pathlib


#Crea la carpeta si no existe
audit_dir = pathlib.Path('logs')
audit_dir.mkdir(exist_ok=True)

#Configuración global
logging.basicConfig(filename=audit_dir/'suite.log', #Ruta del archivo de log
                    level=logging.INFO, # INFO y superiores
                    format='%(asctime)s %(levelname)s - %(message)s',
                    datefmt='%H:%M:%S',
                    force=True)

#Logger específico que usaran los tests
logger = logging.getLogger('talentolab')
