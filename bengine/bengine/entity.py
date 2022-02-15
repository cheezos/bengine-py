import math
import numpy as np
import pyrr
from bengine.entities import Entities
from bengine.window import Window

class Entity:
    def __init__(self, **kwargs) -> None:
        self._children: list[object] = []
        self._parent: object | None = None
        self._name: str = kwargs["name"] if "name" in kwargs else "entity"
        self._position: np.ndarray = np.array([0, 0, 0], dtype=np.float32)
        self._rotation: np.ndarray = np.array([0, 0, 0], dtype=np.float32)

        Entities.add_entity(self)
    
    def add_child(self, child: object) -> None:
        self._children.append(child)
        getattr(child, "set_parent")(self)
        class_name = getattr(child, "class_name")
        print(f"Added {class_name} as child to {self.class_name}")
    
    def remove_child(self, child: object) -> None:
        self._children.remove(child)
    
    def set_parent(self, parent: object) -> None:
        self._parent = parent

    def set_position(self, x: float, y: float, z: float) -> None:
        self._position = np.array([x, y, z], dtype=np.float32)
    
    def set_rotation(self, x: float, y: float, z: float) -> None:
        self._rotation = np.array([x, y, z], dtype=np.float32)

    def translate(self, x: float, y: float, z: float) -> None:
        p = self._position
        self._position = np.array([p[0] + x, p[1] + y, p[2] + z], dtype=np.float32)

    def rotate(self, x: float, y: float, z: float) -> None:
        r = self._rotation
        self._rotation = np.array([r[0] + x, r[1] + y, r[2] + z], dtype=np.float32)

    def destroy(self) -> None:
        pass

    def _process(self, delta_time: float) -> None:
        self._update(delta_time)

        if self._parent is not None:
            p = getattr(self._parent, "position")
            self.set_position(p[0], p[1], p[2])
            r = getattr(self._parent, "rotation")
            self.set_rotation(r[0], r[1], r[2])

    def _update(self, delta_time: float) -> None:
        pass

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, name: str) -> None:
        self._name = name
    
    @property
    def class_name(self) -> str:
        return self.__class__.__name__
    
    @property
    def position(self) -> np.ndarray:
        return self._position
    
    @property
    def rotation(self) -> np.ndarray:
        return self._rotation
    
    @property
    def forward(self) -> np.ndarray:
        z = float(math.sin(math.radians(self._rotation[1] - 90)))
        x = float(math.cos(math.radians(self._rotation[1] - 90)))
        return np.array([x, 0, z], dtype=np.float32)

    @property
    def right(self) -> np.ndarray:
        z = float(math.sin(math.radians(self._rotation[1])))
        x = float(math.cos(math.radians(self._rotation[1])))
        return np.array([x, 0, z], dtype=np.float32)

    @property
    def up(self) -> np.ndarray:
        return pyrr.vector3.cross(self.forward, self.right)

    @property
    def transform_matrix(self) -> np.ndarray:
        r_matrix = pyrr.matrix44.create_from_eulers(self._rotation, dtype=np.float32)
        p_matrix = pyrr.matrix44.create_from_translation(self._position, dtype=np.float32)
        return pyrr.matrix44.multiply(r_matrix, p_matrix)