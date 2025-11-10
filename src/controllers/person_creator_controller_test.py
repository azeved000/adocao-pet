import pytest
from .person_creator_controller import PersonCreatorController

class MockPeopleRepository:
    def insert_person(self, first_name: str, last_name: str, age: int, pet_id: int) -> None:
        pass


def test_create():
    person_info = {
        "first_name": "John",
        "last_name": "Doe",
        "age": 28,
        "pet_id": 112
    }

    controller = PersonCreatorController(MockPeopleRepository())
    response = controller.create_person(person_info)

    assert response["data"]["type"] == "Person"
    assert response["data"]["count"] == 1
    assert response["data"]["attributes"] == person_info


def test_error():
    person_info = {
        "first_name": "John3",
        "last_name": "Doe",
        "age": 28,
        "pet_id": 112
    }

    controller = PersonCreatorController(MockPeopleRepository())
    with pytest.raises(Exception):
        controller.create_person(person_info)
