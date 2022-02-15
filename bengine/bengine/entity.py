import math
import numpy as np
import pyrr
from bengine.entity_manager import EntityManager

class Entity:
    def __init__(self, **kwargs) -> None:
        self._name: str = kwargs["name"] if "name" in kwargs else "entity"
        self._position: np.ndarray = np.array([0, 0, 0], dtype=np.float32)
        self._rotation: np.ndarray = np.array([0, 0, 0], dtype=np.float32)

        EntityManager.add_entity(self)

    def translate(self, x: float, y: float, z: float) -> None:
        p = self._position
        self._position = np.array([p[0] + x, p[1] + y, p[2] + z], dtype=np.float32)

    def set_position(self, x: float, y: float, z: float) -> None:
        self._position = np.array([x, y, z], dtype=np.float32)

    def update(self, delta_time: float) -> None:
        pass

    def destroy(self) -> None:
        pass

    def _process(self, delta_time: float) -> None:
        self.update(delta_time)

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, name: str) -> None:
        self._name = name
    
    @property
    def position(self) -> np.ndarray:
        return self._position
    
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