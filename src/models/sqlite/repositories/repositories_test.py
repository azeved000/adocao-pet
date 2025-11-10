import pytest
from ..settings.connection import db_connection_handler
from ..settings.base import Base
from ..entities.pets import PetsTable  # noqa: F401
from ..entities.people import PeopleTable  # noqa: F401
from .pets_repository import PetsRepository
from .people_repository import PeopleRepository

# Inicializa a conexão para garantir que o engine exista antes da criação das tabelas
# db_connection_handler.connect_to_db()
Base.metadata.create_all(db_connection_handler.get_engine())

@pytest.mark.skip(reason="Interação com o banco de dados")
def test_list_pets():
    repo = PetsRepository(db_connection_handler)
    response = repo.list_pets()
    print()
    print(response) 

@pytest.mark.skip(reason="Interação com o banco de dados")
def test_delete_pets():
    name = "belinha"
    repo = PetsRepository(db_connection_handler)
    repo.delete_pets(name)

@pytest.mark.skip(reason="Interação com o banco de dados")
def test_insert_person():
    first_name = "Teste name"
    last_name = "Teste last name"
    age = 30
    pet_id = 2

    repo = PeopleRepository(db_connection_handler)
    repo.insert_person(first_name, last_name, age, pet_id)

@pytest.mark.skip(reason="Interação com o banco de dados")
def test_get_person():
    person_id = 1

    repo = PeopleRepository(db_connection_handler)
    response = repo.get_person(person_id)
    print()
    print(response)
