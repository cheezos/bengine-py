from bengine.entity_manager import EntityManager
import numpy as np
import pyrr

class Entity:
    def __init__(self, **kwargs) -> None:
        self._name: str = kwargs["name"] if "name" in kwargs else "entity"
        self._position: np.ndarray = kwargs["position"] if "position" in kwargs else np.array([0, 0, 0])
        self._rotation: np.ndarray = kwargs["rotation"] if "rotation" in kwargs else np.array([0, 0, 0])
        self._forward: np.ndarray = np.array([0, 0, 1], dtype=np.float32)
        self._global_up: np.ndarray = np.array([0, 1, 0])
        self._right: np.ndarray = pyrr.vector3.cross(self._global_up, self._forward)
        self._up: np.ndarray = pyrr.vector3.cross(self._forward, self._right)
        self._position_matrix = pyrr.matrix44.create_from_translation(self._position)
        self._rotation_matrix = pyrr.matrix44.create_from_eulers(self._rotation)
        self._transform_matrix = pyrr.matrix44.multiply(self._rotation_matrix, self._position_matrix)

        EntityManager.add_entity(self)

    def _process(self, delta_time: float) -> None:
        self.update(delta_time)

        self._position_matrix = pyrr.matrix44.create_from_translation(self._position)
        self._rotation_matrix = pyrr.matrix44.create_from_eulers(self._rotation)
        self._transform_matrix = pyrr.matrix44.multiply(self._rotation_matrix, self._position_matrix)

    def update(self, delta_time: float) -> None:
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