from dependency_injector import containers, providers

from app.domain.client import DBClient
from app.infra.pokemon_repository import PokemonRepository
from app.usecase.pokemon_usecase import PokemonUsecase


class Container(containers.DeclarativeContainer):
    config = providers.Configuration(yaml_files=["config.yml"])
    config.load()

    db = providers.Singleton(DBClient, db_url=config.db.url())
    pokemon_repo = providers.Factory(PokemonRepository, session_factory=db.provided.session)
    pokemon_usecase = providers.Factory(PokemonUsecase, pokemon_repo=pokemon_repo)
