from bengine.entity_manager import EntityManager
from bengine.vector3 import Vector3

class Entity:
    def __init__(self, **kwargs) -> None:
        self._name = kwargs["name"] if "name" in kwargs else "entity"
        self._position = kwargs["position"] if "position" in kwargs else Vector3(0, 0, 0)
        self._rotation = kwargs["rotation"] if "rotation" in kwargs else Vector3(0, 0, 0)

        EntityManager.add_entity(self)

    def process(self, delta_time: float) -> None:
        self.update(delta_time)

    def update(self, delta_time: float) -> None:
        pass

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, name: str) -> None:
        self._name = name
    
    @property
    def position(self) -> Vector3:
        return self._position
    
    @position.setter
    def position(self, position: Vector3) -> None:
        self._position = position
    
    @property
    def rotation(self) -> Vector3:
        return self._rotation
    
    @rotation.setter
    def rotation(self, rotation: Vector3) -> None:
        self._rotation = rotation