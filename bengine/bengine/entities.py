class Entities(object):
    _entities: list[object] = []

    @staticmethod
    def add_entity(entity: object) -> None:
        Entities._entities.append(entity)

    @staticmethod
    def update(delta_time: float) -> None:
        for entity in Entities._entities:
            getattr(entity, "_process")(delta_time)
    
    @staticmethod
    def cleanup() -> None:
        for entity in Entities._entities:
            getattr(entity, "destroy")()