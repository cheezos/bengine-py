from bengine.entity import Entity
from bengine.input import Input
from bengine.engine import Engine
from bengine.window import Window
import glfw
import numpy as np

class Freecam(Entity):
    def __init__(self, **kwargs) -> None:
        __name__ = "Freecam"
        super().__init__(**kwargs)

        self.add_child(Engine.get_camera())
        Input.set_cursor_state(glfw.CURSOR_DISABLED)

        self.last_mouse_pos: tuple[float, float] = (0, 0)

        
    def _update(self, delta_time: float) -> None:
        self._handle_keeb(delta_time)
        self._handle_mouse(delta_time)

    def _handle_keeb(self, delta_time: float) -> None:
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

    def _handle_mouse(self, delta_time: float) -> None:
        mx = Input.get_mouse_position()[0]
        my = Input.get_mouse_position()[1]
        dy = mx - self.last_mouse_pos[0]
        dx = my - self.last_mouse_pos[1]
        self.last_mouse_pos = (mx, my)
        self.rotate(dx * delta_time * 5, -dy * delta_time * 5, 0)

        if self.rotation.x > 85:
            self.rotation.x = 85
        
        if self.rotation.x < -85:
            self.rotation.x = -85