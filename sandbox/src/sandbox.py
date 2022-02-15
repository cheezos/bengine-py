from bengine.engine import Engine
from bengine.game import Game
from bengine.mesh_instance import MeshInstance
from bengine.prefabs.freecam import Freecam

class Sandbox(Game):
    def __init__(self) -> None:
        Engine.init(self, "Sandbox")

    def init(self) -> None:
        self.m = MeshInstance("models/b.obj")
        self.m.translate(0, 0, -5)
        self.c = Freecam()

    def update(self, delta_time: float) -> None:
        pass
        # Engine.get_camera().rotate(delta_time, 0, 0)

    def quit(self) -> None: pass

Sandbox()