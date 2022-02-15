from bengine.entity import Entity
from bengine.window import Window
import pyrr
import numpy as np

class Camera(Entity):
    def __init__(self, **kwargs) -> None:
        __name__ = "Camera"
        super().__init__(**kwargs)

        self._fov = 90
        self._view_distance = 1000

    @property
    def projection_matrix(self) -> np.ndarray:
        return pyrr.matrix44.create_perspective_projection_matrix(
            self._fov, Window.get_size()[0] / Window.get_size()[1], 0.01, self._view_distance, dtype=np.float32)
    
    @property
    def view_matrix(self) -> np.ndarray:
        return pyrr.matrix44.create_look_at(
            self._position, self._position + self.forward, self.up, dtype=np.float32)
