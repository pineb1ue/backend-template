from loguru import logger

from app.domain.infra.pokemon_repository import IPokemonRepository
from app.domain.orm import PokemonOrm


class PokemonUsecase:
    def __init__(self, pokemon_repo: IPokemonRepository) -> None:
        self._pokemon_repo = pokemon_repo

    def get_all(self) -> list[PokemonOrm]:
        logger.info("Start - PokemonUsecase.get_all")
        pokemons = self._pokemon_repo.get_all()
        logger.info("End - PokemonUsecase.get_all")
        return pokemons

    def get_by_no(self, pokemon_no: str) -> PokemonOrm:
        logger.info("Start - PokemonUsecase.get_by_no")
        pokemon = self._pokemon_repo.get_by_no(pokemon_no)
        logger.info("End - PokemonUsecase.get_by_no")
        return pokemon

    def add(self, pokemon: PokemonOrm) -> None:
        logger.info("Start - PokemonUsecase.add")
        self._pokemon_repo.add(pokemon)
        logger.info("End - PokemonUsecase.add")

    def delete_by_no(self, pokemon_no: str) -> None:
        logger.info("Start - PokemonUsecase.delete_by_no")
        self._pokemon_repo.delete_by_no(pokemon_no)
        logger.info("End - PokemonUsecase.delete_by_no")
