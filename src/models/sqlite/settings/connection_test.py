from sqlalchemy.engine import Engine
from .connection import db_connection_handler

def test_connect_to_db():
    # Conecta ao banco de dados (se já não estiver conectado)
    db_connection_handler.connect_to_db()
    db_engine = db_connection_handler.get_engine()

    assert db_engine is not None
    assert isinstance(db_engine, Engine)