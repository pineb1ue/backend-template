from contextlib import AbstractContextManager
from sqlite3 import IntegrityError
from typing import Callable

from loguru import logger
from sqlalchemy.orm import Session

from app.domain.exception import PokemonIntegrityError, PokemonNotFoundError
from app.domain.infra.pokemon_repository import IPokemonRepository
from app.domain.orm import PokemonOrm


class PokemonRepository(IPokemonRepository):
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self._session_factory = session_factory

    def get_all(self) -> list[PokemonOrm]:
        with self._session_factory() as session:
            return session.query(PokemonOrm).all()

    def get_by_no(self, pokemon_no: str) -> PokemonOrm:
        with self._session_factory() as session:
            logger.info("Start - PokemonRepository.get_by_no")
            pokemon = session.query(PokemonOrm).filter(PokemonOrm.no == pokemon_no).first()
            if not pokemon:
                raise PokemonNotFoundError(pokemon_no)
            logger.info("End - PokemonRepository.get_by_no")
            return pokemon

    def add(self, pokemon: PokemonOrm) -> PokemonOrm:
        with self._session_factory() as session:
            try:
                logger.info("Start - PokemonRepository.add")
                session.add(pokemon)
                session.commit()
                session.refresh(pokemon)
                logger.info("End - PokemonRepository.add")
                return pokemon
            except IntegrityError:
                raise PokemonIntegrityError()
            except Exception as e:
                logger.error(f"Error - PokemonRepository.add: {e}")
                session.rollback()
                raise

    def delete_by_no(self, pokemon_no: str) -> None:
        with self._session_factory() as session:
            logger.info("Start - PokemonRepository.delete_by_no")
            pokemon = session.query(PokemonOrm).filter(PokemonOrm.no == pokemon_no).first()
            if not pokemon:
                raise PokemonNotFoundError(pokemon_no)
            session.delete(pokemon)
            session.commit()
            logger.info("End - PokemonRepository.delete_by_no")
