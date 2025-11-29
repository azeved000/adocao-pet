import sys
from pathlib import Path

# Adiciona o diretório raiz ao path
root_path = Path(__file__).parent
sys.path.insert(0, str(root_path))

from src.main.server.server import app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)  