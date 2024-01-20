from pydantic import BaseModel, ConfigDict, StringConstraints
from typing_extensions import Annotated


class Pokemon(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    no: Annotated[str, StringConstraints(max_length=31)]
    name: Annotated[str, StringConstraints(max_length=127)]
    class_name: Annotated[str, StringConstraints(max_length=127)]
    type1: Annotated[str, StringConstraints(max_length=127)]
    type2: Annotated[str, StringConstraints(max_length=127)]
    height: Annotated[str, StringConstraints(max_length=127)]
    weight: Annotated[str, StringConstraints(max_length=127)]
