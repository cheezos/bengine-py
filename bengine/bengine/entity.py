import math
from bengine.entity_manager import EntityManager
import numpy as np
import pyrr

class Entity:
    def __init__(self, **kwargs) -> None:
        self._name: str = kwargs["name"] if "name" in kwargs else "entity"
        self._position: np.ndarray = kwargs["position"] if "position" in kwargs else np.array([0, 0, 0], dtype=np.float32)
        self._rotation: np.ndarray = kwargs["rotation"] if "rotation" in kwargs else np.array([0, 0, 0], dtype=np.float32)

        EntityManager.add_entity(self)

    def _process(self, delta_time: float) -> None:
        self.update(delta_time)

    def update(self, delta_time: float) -> None:
        pass

    def destroy(self) -> None:
        pass

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, name: str) -> None:
        self._name = name
    
    @property
    def position(self) -> np.ndarray:
        return self._position
    
    @position.setter
    def position(self, position: np.ndarray) -> None:
        self._position = position
    
    @property
    def rotation(self) -> np.ndarray:
        return self._rotation
    
    @rotation.setter
    def rotation(self, rotation: np.ndarray) -> None:
        self._rotation = rotation
    
    @property
    def forward(self) -> np.ndarray:
        z = float(math.sin(math.radians(self._rotation[1] - 90)))
        x = float(math.cos(math.radians(self._rotation[1] - 90)))
        return np.array([x, 0, z], dtype=np.float32)

    @property
    def right(self) -> np.ndarray:
        return pyrr.vector3.cross(np.array([0, 1, 0], dtype=np.float32), self.forward)

    @property
    def up(self) -> np.ndarray:
        return pyrr.vector3.cross(self.forward, self.right)

    @property
    def transform_matrix(self) -> np.ndarray:
        return pyrr.matrix44.create_from_translation(self._position, dtype=np.float32)