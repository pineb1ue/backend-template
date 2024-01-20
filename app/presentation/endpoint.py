from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Response, status

from app.domain.container import Container
from app.domain.exception import PokemonNotFoundError
from app.domain.model import Pokemon
from app.domain.orm import PokemonOrm
from app.usecase.pokemon_usecase import PokemonUsecase

router = APIRouter()


@router.get("/pokemon")
@inject
async def get_all_pokemons(
    pokemon_usecase: PokemonUsecase = Depends(Provide[Container.pokemon_usecase]),
):
    try:
        pokemons = pokemon_usecase.get_all()
        return [Pokemon.model_validate(pokemon) for pokemon in pokemons]
    except Exception:
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@router.get("/pokemon/{pokemon_no}")
@inject
async def get_pokemon_by_pokemon_no(
    pokemon_no: str,
    pokemon_usecase: PokemonUsecase = Depends(Provide[Container.pokemon_usecase]),
):
    try:
        return Pokemon.model_validate(pokemon_usecase.get_by_no(pokemon_no))
    except PokemonNotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    except Exception:
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@router.post("/pokemon")
@inject
async def add_pokemon(
    pokemon: Pokemon,
    pokemon_usecase: PokemonUsecase = Depends(Provide[Container.pokemon_usecase]),
):
    try:
        pokemon_usecase.add(PokemonOrm(**pokemon.model_dump()))
    except Exception:
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@router.delete("/pokemon/{pokemon_no}")
@inject
async def remove_pokemon_by_pokemon_no(
    pokemon_no: str,
    pokemon_usecase: PokemonUsecase = Depends(Provide[Container.pokemon_usecase]),
):
    try:
        pokemon_usecase.delete_by_no(pokemon_no)
    except PokemonNotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    except Exception:
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
