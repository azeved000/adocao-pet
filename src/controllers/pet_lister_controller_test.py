from src.models.sqlite.entities.pets import PetsTable
from src.controllers.pet_lister_controller import PetListerController

class MockPetsRepository:
    def list_pets(self) :
        return [
            PetsTable(name="Fido", type="dog", id=4),
            PetsTable(name="Whiskers", type="cat", id=3)
        ]

def test_list_pets():
    controller = PetListerController(MockPetsRepository())
    response = controller.list()

    expected_response = {
        "data": {
            "type": "Pets",
            "count": 2,
            "attributes": [
                {"name": "Fido", "id": 4},
                {"name": "Whiskers", "id": 3}
            ]
        }
    }

    assert response == expected_response
