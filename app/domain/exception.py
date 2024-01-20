class NotFoundError(Exception):
    entity_name: str

    def __init__(self, entity_no: str) -> None:
        super().__init__(f"{self.entity_name} not found, no: {entity_no}")


class IntegrityError(Exception):
    entity_name: str

    def __init__(self) -> None:
        super().__init__(f"{self.entity_name} already exists")


class PokemonNotFoundError(NotFoundError):
    entity_name: str = "PokemonOrm"


class PokemonIntegrityError(IntegrityError):
    entity_name: str = "PokemonOrm"
