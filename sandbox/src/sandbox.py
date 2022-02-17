from bengine.engine import Engine
from bengine.game import Game
from bengine.mesh_instance import MeshInstance
from bengine.prefabs.freecam import Freecam
import os

class Main(Game):
    def __init__(self) -> None:
        root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        Engine.init(self, root)

    def init(self) -> None:
        self.c = Freecam()
        self.f = MeshInstance("floor.obj", "base2.png", "unlit")
        self.f.translate(0, -3, 0)
        self.b = MeshInstance("b.obj", "base.png", "unlit")
        self.b.translate(0, 0, -5)
        
    def update(self, delta_time: float) -> None:
        self.b.rotate(delta_time, delta_time, delta_time)

    def quit(self) -> None: pass

if __name__ == "__main__":
    main = Main()