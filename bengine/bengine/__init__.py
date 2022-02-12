import threading
import sys
import time
import glfw
from bengine.input import Input
from bengine.window import Window
from bengine.game import Game

_game: Game | None = None
_quit: bool = False

def init(game: Game) -> None:
    global _game
    _game = game        

    engine_thread = threading.Thread(target=_initialize_engine)
    engine_thread.start()

    game_thread = threading.Thread(target=_initialize_game)
    game_thread.start()

def _initialize_engine() -> None:
    Window.create_window(0, 1080)

    assert _game is not None
    _game.on_init()

    while not _should_close():
        Window.update()

    _cleanup()

def _initialize_game() -> None:
    assert _game is not None
    
    while not _should_close():
        _game.on_update(Window.get_delta_time())

    _game.on_quit()

def _cleanup() -> None:
    print("Cleaning up...")

    Window.cleanup()
    sys.exit()

def _should_close() -> bool:
    global _quit

    if Window.get_window() is None:
        return True
    
    if glfw.window_should_close(Window.get_window()):
        _quit = True

    if Input.is_action_just_pressed(glfw.KEY_ESCAPE):
        _quit = True

    return _quit