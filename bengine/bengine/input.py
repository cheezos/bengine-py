import glfw
from bengine.window import Window

class Input(object):
    _pressed_keys: list[int] = []
    _cursor_state: int = glfw.CURSOR_NORMAL
    _mouse_position: tuple[float, float] = (0.0, 0.0)

    @staticmethod
    def init() -> None:
        if glfw.raw_mouse_motion_supported():
            glfw.set_input_mode(Window.get_window(), glfw.RAW_MOUSE_MOTION, glfw.TRUE)
        
        glfw.set_cursor_pos_callback(Window.get_window(), lambda _, x, y: Input._mouse_pos_callback(x, y))

    @staticmethod
    def is_action_pressed(action: int) -> bool:
        if glfw.get_key(Window.get_window(), action):
            if action not in Input._pressed_keys:
                Input._pressed_keys.append(action)
                
            return True
        else:
            if action in Input._pressed_keys:
                Input._pressed_keys.remove(action)
        
        return False

    @staticmethod
    def is_action_just_pressed(action: int) -> bool:
        if glfw.get_key(Window.get_window(), action):
            if action not in Input._pressed_keys:
                Input._pressed_keys.append(action)
                
                return True
        else:
            if action in Input._pressed_keys:
                Input._pressed_keys.remove(action)

        return False

    @staticmethod
    def set_cursor_state(state: int) -> None:
        glfw.set_cursor_pos(
            Window.get_window(),
            glfw.get_window_size(Window.get_window())[0] / 2,
            glfw.get_window_size(Window.get_window())[1] / 2
        )
    
        glfw.set_input_mode(Window.get_window(), glfw.CURSOR, state)
        Input._cursor_state = state

    @staticmethod
    def get_cursor_state() -> int:
        return Input._cursor_state

    @staticmethod
    def get_mouse_position() -> tuple[float, float]:
        return Input._mouse_position
    
    @staticmethod
    def _mouse_pos_callback(x: float, y: float) -> None:
        Input._mouse_position = (x, y)