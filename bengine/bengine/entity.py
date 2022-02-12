from bengine.entities import Entities


class Entity:
    def __init__(self, **args) -> None:
        self.name = args["name"] if "name" in args else "entity"

        print(self.name)

        Entities.add_entity(self)