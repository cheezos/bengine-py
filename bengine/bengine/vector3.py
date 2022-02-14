import numpy as np

class Vector3:
    def __init__(self, x: float, y: float, z: float) -> None:
        self._vector: np.ndarray = np.array([x, y, z], dtype=np.float32)
    
    @property
    def x(self) -> float:
        return self._vector[0]
    
    @property
    def y(self) -> float:
        return self._vector[1]

    @property
    def z(self) -> float:
        return self._vector[2]