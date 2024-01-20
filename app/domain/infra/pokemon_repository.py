from abc import ABC, abstractmethod

from app.domain.orm import PokemonOrm


class IPokemonRepository(ABC):
    @abstractmethod
    def get_all(self) -> list[PokemonOrm]:
        pass

    @abstractmethod
    def get_by_no(self, pokemon_no: str) -> PokemonOrm:
        pass

    @abstractmethod
    def add(self, pokemon: PokemonOrm) -> PokemonOrm:
        pass

    @abstractmethod
    def delete_by_no(self, pokemon_no: str) -> None:
        pass
