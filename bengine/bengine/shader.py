from OpenGL.GL import shaders
from bengine.loader import Loader

class Shader:
    def __init__(self, vertex_code: str, fragment_code: str) -> None:
        self._program: shaders.ShaderProgram = Loader.load_shader(vertex_code, fragment_code)

    @property
    def program(self) -> shaders.ShaderProgram:
        return self._program