from bengine.entity import Entity
from bengine.input import Input
from bengine.engine import Engine
import glfw
import numpy as np

class Freecam(Entity):
    def __init__(self, **kwargs) -> None:
        __name__ = "Freecam"
        super().__init__(**kwargs)

        self.add_child(Engine.get_camera())
        Input.set_cursor_state(glfw.CURSOR_DISABLED)
        
    def _update(self, delta_time: float) -> None:
        if Input.is_action_pressed(glfw.KEY_W):
            pos = np.multiply(self.forward, delta_time * 10)
            self.translate(pos[0], pos[1], pos[2])
        
        if Input.is_action_pressed(glfw.KEY_S):
            pos = np.multiply(self.forward, -1 * delta_time * 10)
            self.translate(pos[0], pos[1], pos[2])
        
        if Input.is_action_pressed(glfw.KEY_A):
            pos = np.multiply(self.right, delta_time * 10)
            self.translate(pos[0], pos[1], pos[2])
        
        if Input.is_action_pressed(glfw.KEY_D):
            pos = np.multiply(self.right, -1 * delta_time * 10)
            self.translate(pos[0], pos[1], pos[2])

        if Input.get_cursor_state() == glfw.CURSOR_DISABLED:
            self.rotate(Input.get_mouse_delta()[1] * delta_time * 50, Input.get_mouse_delta()[0] * delta_time * 50, 0)