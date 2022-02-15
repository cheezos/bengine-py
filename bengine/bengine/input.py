import glfw
from bengine.window import Window

class Input(object):
    _pressed_keys: list[int] = []
    _cursor_state: int = glfw.CURSOR_NORMAL
    _mouse_last_pos: tuple[float, float] = (0, 0)
    _mouse_delta: tuple[float, float] = (0, 0)

    @staticmethod
    def init() -> None:
        glfw.set_cursor_pos_callback(Window.get_window(), lambda _, x, y: Input._mouse_callback(x, y))

    @staticmethod
    def end_frame() -> None:
        Input._mouse_delta = (0, 0)

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
    def get_mouse_delta() -> tuple[float, float]:
        return Input._mouse_delta
    
    @staticmethod
    def _mouse_callback(x: float, y: float) -> None:
        d_x = x - Input._mouse_last_pos[0]
        d_y = y - Input._mouse_last_pos[1]
        Input._mouse_delta = (d_x, d_y)
        Input._mouse_last_pos = (x, y)