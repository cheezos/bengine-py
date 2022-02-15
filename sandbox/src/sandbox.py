import bengine
from bengine.mesh_instance import MeshInstance

class Sandbox(bengine.Game):
    def __init__(self) -> None:
        bengine.init(self, "Sandbox")

    def init(self) -> None:
        self.m = MeshInstance("models/b.obj")
        self.m.translate(0, 0, -5)

    def update(self, delta_time: float) -> None:
        self.m.translate(delta_time, 0, 0)
        pass

    def quit(self) -> None:
        print("quitted")

Sandbox()