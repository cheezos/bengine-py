import sys
import glfw
from window import Window


class Main:
    def __init__(self) -> None:
        Window.create_window(1920, 1080)

        self.update()

    def update(self) -> None:
        while not glfw.window_should_close(Window.window):
            Window.update()

            Window.end_frame()

        self.cleanup()

    def cleanup(self) -> None:
        print("Cleaning up...")

        Window.cleanup()
        sys.exit()

if __name__ == "__main__":
    main = Main()