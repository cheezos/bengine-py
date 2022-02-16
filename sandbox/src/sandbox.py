from bengine.engine import Engine
from bengine.game import Game
from bengine.mesh_instance import MeshInstance
from bengine.prefabs.freecam import Freecam
import os

class Sandbox(Game):
    def __init__(self) -> None:
        root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        Engine.init(self, root)

    def init(self) -> None:
        self.c = Freecam()
        self.b1 = MeshInstance("b.obj", "base.png", "unlit")
        self.b1.translate(0, 0, -5)
        self.b2 = MeshInstance("b.obj", "base2.png", "unlit")
        self.b2.translate(0, 0, 5)
        self.f = MeshInstance("floor.obj", "base.png", "unlit")
        self.f.translate(0, -3, 0)

        for x in range(-3, 3, 1):
            for y in range(-3, 3, 1):
                m = MeshInstance("b.obj", "base2.png", "unlit")
                m.translate(x * 2, 5, y * 2)

    def update(self, delta_time: float) -> None:
        self.b1.rotate(delta_time, delta_time, delta_time)
        self.b2.rotate(-delta_time, -delta_time, -delta_time)

    def quit(self) -> None: pass

main = Sandbox()