import threading
import sys
import glfw
from bengine.window import Window
from bengine.input import Input
from bengine.game import Game
from bengine.entities import Entities
from bengine.loader import Loader
from bengine.camera import Camera

class Engine(object):
    _game: Game
    _camera: Camera
    _quit: bool = False

    @staticmethod
    def init(game: Game, title: str) -> None:
        Engine._game = game
        
        engine_thread = threading.Thread(target=Engine._start_engine, args=(title,))
        engine_thread.start()

    @staticmethod
    def _start_engine(title: str) -> None:
        assert Engine._game is not None

        Window.create_window(title, 1920, 1080)
        Input.init()
        Engine._camera = Camera()
        Engine._game.init()

        while not Engine._should_close():
            Window.update()
            Entities.update(Window.get_delta_time())
            Engine._game.update(Window.get_delta_time())
            Input.end_frame()

        Engine._cleanup()

    @staticmethod
    def _cleanup() -> None:
        print("Cleaning up...")

        Engine._game.quit()
        Entities.cleanup()
        Loader.cleanup()
        Window.cleanup()
        sys.exit()

    @staticmethod
    def _should_close() -> bool:
        if Window.get_window() is None:
            return True
        
        if glfw.window_should_close(Window.get_window()):
            Engine._quit = True

        if Input.is_action_just_pressed(glfw.KEY_ESCAPE):
            Engine._quit = True

        return Engine._quit

    @staticmethod
    def get_camera() -> Camera:
        return Engine._camera