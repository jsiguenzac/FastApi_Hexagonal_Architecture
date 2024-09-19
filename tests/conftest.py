import sys
import os

# se adecúa el directorio de raíz del proyecto para que pytest pueda importar los módulos de src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))