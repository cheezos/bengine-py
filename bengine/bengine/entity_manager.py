

class EntityManager(object):
    _entities: list[object] = []

    @staticmethod
    def add_entity(entity: object) -> None:
        EntityManager._entities.append(entity)

    @staticmethod
    def update(delta_time: float) -> None:
        for entity in EntityManager._entities:
            entity.process(delta_time)