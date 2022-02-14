import threading
import sys
import glfw
from bengine.window import Window
from bengine.input import Input
from bengine.game import Game
from bengine.entity_manager import EntityManager
from bengine.loader import Loader

_game: Game | None = None
_quit: bool = False

def init(game: Game, title: str) -> None:
    global _game
    _game = game        

    engine_thread = threading.Thread(target=_initialize_engine, args=(title,))
    engine_thread.start()

    game_thread = threading.Thread(target=_initialize_game)
    game_thread.start()

def _initialize_engine(title: str) -> None:
    Window.create_window(title, 1280, 720)

    assert _game is not None
    _game.on_init()

    while not _should_close():
        Window.update()
        EntityManager.update(Window.get_delta_time())

    _cleanup()

def _initialize_game() -> None:
    assert _game is not None
    
    while not _should_close():
        _game.on_update(Window.get_delta_time())

    _game.on_quit()

def _cleanup() -> None:
    print("Cleaning up...")

    Window.cleanup()
    Loader.cleanup()
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