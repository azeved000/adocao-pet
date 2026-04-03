import sys
import os

# Adiciona o diretório do projeto ao path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.main.server.server import app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)  