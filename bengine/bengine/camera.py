from bengine.entity import Entity
from bengine.window import Window
import glfw, pyrr
import numpy as np

class Camera(Entity):
    def __init__(self, **kwargs) -> None:
        __name__ = "Camera"
        super().__init__(**kwargs)

        self._fov = 90
        self._view_distance = 1000
        
        self._projection = pyrr.matrix44.create_perspective_projection_matrix(
            self._fov, Window.get_size()[0] / Window.get_size()[1], 0.01, self._view_distance)
        
        self._view = pyrr.matrix44.create_look_at(
            self._position, self._position + self._forward, self._up, dtype=np.float32)
    
    def _process(self, delta_time: float) -> None:
        super()._process(delta_time)

        self._projection = pyrr.matrix44.create_perspective_projection_matrix(
            self._fov, Window.get_size()[0] / Window.get_size()[1], 0.01, self._view_distance)
        
        self._view = pyrr.matrix44.create_look_at(
            self._position, self._position + self._forward, self._up, dtype=np.float32)