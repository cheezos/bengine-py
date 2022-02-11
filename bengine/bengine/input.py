import glfw

from bengine.window import Window

class Input(object):
    _pressed_keys: list[int] = []
    _cursor_state: int = glfw.CURSOR_NORMAL

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
        Input.cursor_state = state