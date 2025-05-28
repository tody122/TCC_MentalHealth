import sys
import os

# Adiciona o diretório raiz ao PYTHONPATH
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from Backend.TCC_FINAL import app

if __name__ == "__main__":
    app.run() 