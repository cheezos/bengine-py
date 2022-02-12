import threading
import sys
import glfw
from bengine.input import Input
from bengine.window import Window
from bengine.game import Game

_game: Game | None = None

def init(game: Game) -> None:
    global _game
    _game = game

    def create_thread(game: Game):
        Window.create_window(1920, 1080)
        game.on_init()
        update()

    thread = threading.Thread(target=create_thread, args=(_game,))
    thread.start()

def update() -> None:
    while not glfw.window_should_close(Window.get_window()):
        Window.update()

        if (_game != None):
            _game.on_update(Window.get_delta_time())

        if should_close():
            break

    cleanup()

def cleanup() -> None:
    print("Cleaning up...")

    Window.cleanup()
    sys.exit()

def should_close() -> bool:
    return Input.is_action_just_pressed(glfw.KEY_ESCAPE)