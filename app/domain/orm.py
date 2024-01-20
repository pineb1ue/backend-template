from sqlalchemy import Column, String

from app.domain.client import Base


class PokemonOrm(Base):
    __tablename__ = "pokemons"

    no = Column(String(31), primary_key=True, nullable=False)
    name = Column(String(127), unique=True, nullable=False)
    class_name = Column(String(127))
    type1 = Column(String(127))
    type2 = Column(String(127))
    height = Column(String(127))
    weight = Column(String(127))

    def __repr__(self) -> str:
        return (
            f"<PokemonOrm(no={self.no}, "
            f'name="{self.name}", '
            f'class_name="{self.class_name}", '
            f'type1="{self.type1}", '
            f'type2="{self.type2}", '
            f'height="{self.height}", '
            f"weight={self.weight})>"
        )
