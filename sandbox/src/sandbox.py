from bengine.engine import Engine
from bengine.game import Game
from bengine.mesh_instance import MeshInstance
from bengine.prefabs.freecam import Freecam
import os

class Sandbox(Game):
    def __init__(self) -> None:
        super().__init__(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        Engine.init(self)

    def init(self) -> None:
        c = Freecam()
        self.b = MeshInstance("models/b.obj")
        self.b.translate(0, 0, -5)
        self.f = MeshInstance("models/floor.obj")
        self.f.translate(0, -3, 0)

    def update(self, delta_time: float) -> None:
        # Engine.get_camera().rotate(delta_time, 0, 0)
        self.b.rotate(delta_time, delta_time, delta_time)

    def quit(self) -> None: pass

Sandbox()