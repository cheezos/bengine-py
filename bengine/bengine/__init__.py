import threading
import sys
import glfw
from typing import Callable
from bengine.input import Input
from bengine.window import Window

def init(callback: Callable) -> None:
    def create_thread():
        Window.create_window(1920, 1080)
        callback()
        update()

    thread = threading.Thread(target=create_thread)
    thread.start()


def update() -> None:
    while not glfw.window_should_close(Window.get_window()):
        Window.update()

        if should_close():
            break

    cleanup()

def cleanup() -> None:
    print("Cleaning up...")

    Window.cleanup()
    sys.exit()

def should_close() -> bool:
    return Input.is_action_just_pressed(glfw.KEY_ESCAPE)