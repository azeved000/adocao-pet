from src.models.sqlite.interfaces.people_repository import PeopleRepositoryInterface

class PersonCreatorController:
    def __init__(self, person_repository: PeopleRepositoryInterface) -> None:
        self.__person_repository = person_repository