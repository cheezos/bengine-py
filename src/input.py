import glfw

from window import Window

class Input(object):
    pressed_keys: list[int] = []
    cursor_state: int = glfw.CURSOR_NORMAL

    @staticmethod
    def is_action_pressed(action: int) -> bool:
        if glfw.get_key(Window.window, action):
            if action not in Input.pressed_keys:
                Input.pressed_keys.append(action)
                
            return True
        else:
            if action in Input.pressed_keys:
                Input.pressed_keys.remove(action)
        
        return False

    @staticmethod
    def is_action_just_pressed(action: int) -> bool:
        if glfw.get_key(Window.window, action):
            if action not in Input.pressed_keys:
                Input.pressed_keys.append(action)
                
                return True
        else:
            if action in Input.pressed_keys:
                Input.pressed_keys.remove(action)

        return False

    @staticmethod
    def set_cursor_state(state: int) -> None:
        glfw.set_cursor_pos(
            Window.window,
            glfw.get_window_size(Window.window)[0] / 2,
            glfw.get_window_size(Window.window)[1] / 2
        )
    
        glfw.set_input_mode(Window.window, glfw.CURSOR, state)
        Input.cursor_state = state