import threading
import sys
import glfw
from bengine.input import Input
from bengine.window import Window
from bengine.game import Game

_game: Game | None = None
_should_close: bool = False

def init(game: Game) -> None:
    global _game
    _game = game        

    engine_thread = threading.Thread(target=start_engine_update)
    engine_thread.start()

    game_thread = threading.Thread(target=start_game_update)
    game_thread.start()

def start_engine_update() -> None:
    Window.create_window(1920, 1080)

    assert _game is not None
    _game.on_init()

    while not should_close():
        Window.update()

    cleanup()

def start_game_update() -> None:
    assert _game is not None
    
    while not should_close():
        _game.on_update(Window.get_delta_time())

def cleanup() -> None:
    print("Cleaning up...")

    Window.cleanup()
    sys.exit()

def should_close() -> bool:
    global _should_close
    
    if glfw.window_should_close(Window.get_window()):
        _should_close = True

    if Input.is_action_just_pressed(glfw.KEY_ESCAPE):
        _should_close = True

    return _should_close