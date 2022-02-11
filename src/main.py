import sys
import glfw
from input import Input
from window import Window

class Main:
    def __init__(self) -> None:
        Window.create_window(1920, 1080)
        Input.set_cursor_state(glfw.CURSOR_DISABLED)

        self.update()

    def update(self) -> None:
        while not glfw.window_should_close(Window.window):
            Window.update()

            if Input.is_action_just_pressed(glfw.KEY_W):
                print("pressed")

            Window.end_frame()

        self.cleanup()

    def cleanup(self) -> None:
        print("Cleaning up...")

        Window.cleanup()
        sys.exit()

if __name__ == "__main__":
    main = Main()