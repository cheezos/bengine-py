import sys
import glfw
from bengine.window import Window
from bengine.input import Input
from bengine.game import Game
from bengine.entities import Entities
from bengine.loader import Loader
from bengine.camera import Camera
from bengine.debug import Debug

class Engine(object):
    _game: Game
    _camera: Camera
    _quit: bool = False

    @staticmethod
    def init(game: Game, game_root_directory: str) -> None:
        """Initializes the game engine.

        Args:
            game (Game): The game class.
            game_root_directory (str): The game's root directory.
        """
        Engine._game = game

        Window.create_window(Engine._game.__class__.__name__, 1920, 1080)
        Loader.init(game_root_directory)
        Input.init()
        Engine._camera = Camera()
        Engine._game.init()

        while not Engine._should_close():
            Window.update()
            Debug.update()
            Entities.update(Window.get_delta_time())
            Engine._game.update(Window.get_delta_time())
            Input.end_frame()

        Engine._cleanup()

    @staticmethod
    def _cleanup() -> None:
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