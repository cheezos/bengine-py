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
        self._position: pyrr.Vector3 = pyrr.Vector3([0, 0, 0], dtype=np.float32)
        self._rotation: pyrr.Vector3 = pyrr.Vector3([0, 0, 0], dtype=np.float32)

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
        self._position = pyrr.Vector3([x, y, z])
    
    def set_rotation(self, x: float, y: float, z: float) -> None:
        self._rotation = pyrr.Vector3([x, y, z])

    def translate(self, x: float, y: float, z: float) -> None:
        self._position.x += x
        self._position.y += y
        self._position.z += z

    def rotate(self, x: float, y: float, z: float) -> None:
        self._rotation.x += x
        self._rotation.y += y
        self._rotation.z += z

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
    def position(self) -> pyrr.Vector3:
        return self._position
    
    @property
    def rotation(self) -> pyrr.Vector3:
        return self._rotation
    
    @property
    def forward(self) -> pyrr.Vector3:
        vec = pyrr.Vector3([0, 0, 0], dtype=np.float32)
        vec.x = math.cos(math.radians(self._rotation.y)) * math.cos(math.radians(self._rotation.x))
        vec.y = math.sin(math.radians(self._rotation.x))
        vec.z = math.sin(math.radians(self._rotation.y)) * math.cos(math.radians(self._rotation.x))
        vec = pyrr.vector.normalise(vec)
        return vec

    @property
    def right(self) -> pyrr.Vector3:
        vec = pyrr.Vector3([0, 0, 0], dtype=np.float32)
        vec.x = math.cos(math.radians(self._rotation.y)) * math.cos(math.radians(self._rotation.x))
        vec.y = math.sin(math.radians(self._rotation.x))
        vec.z = math.sin(math.radians(self._rotation.y)) * math.cos(math.radians(self._rotation.x))
        vec = pyrr.vector3.cross(self.forward, pyrr.Vector3([0, 1, 0], dtype=np.float32))
        vec = pyrr.vector.normalise(vec)
        return vec

    @property
    def up(self) -> pyrr.Vector3:
        vec = pyrr.vector3.cross(self.forward, self.right)
        vec = pyrr.vector.normalise(vec)
        return vec

    @property
    def transform_matrix(self) -> np.ndarray:
        pos = self._position
        r_matrix = pyrr.matrix44.create_from_eulers(self._rotation, dtype=np.float32)
        p_matrix = pyrr.matrix44.create_from_translation([pos[0], -pos[1], pos[2]], dtype=np.float32)
        vec = pyrr.matrix44.multiply(r_matrix, p_matrix)
        return vec