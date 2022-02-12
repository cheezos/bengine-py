

class Entities(object):
    _entities: list[object] = []

    @staticmethod
    def add_entity(entity: object) -> None:
        Entities._entities.append(entity)