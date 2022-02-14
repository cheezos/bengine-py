import bengine
import numpy as np
from bengine.mesh_instance import MeshInstance

class Sandbox(bengine.Game):
    def __init__(self) -> None:
        bengine.init(self, "Sandbox")

    def on_init(self) -> None:
        MeshInstance("models/b.obj", position=np.array([0, 0, -5]))

    def on_update(self, delta_time: float) -> None:
        pass

    def on_quit(self) -> None:
        pass

Sandbox()