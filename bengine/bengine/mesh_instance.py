import ctypes
import numpy as np
from OpenGL import GL
from bengine.entity import Entity
from bengine.model import Model
from bengine.texture import Texture
from bengine.shader import Shader
from bengine.obj_loader import OBJLoader
from bengine.resources.shaders.unlit_shader import UnlitShaderSource

class MeshInstance(Entity):
    def __init__(self, model_path: str, **kwargs) -> None:
        __name__ = "MeshInstance"
        super().__init__(**kwargs)

        self._vertices: np.ndarray = np.array([0, 1, 2])
        self._vertex_count: int = int(len(self._vertices) / 8)
        self._model: Model = Model(model_path)
        self._texture: Texture = Texture("textures/base.png")
        self._shader: Shader = Shader(UnlitShaderSource.vertex_shader, UnlitShaderSource.fragment_shader)        

    def set_model(self, model_path: str) -> None:
        self._vertices = OBJLoader.load(model_path)
        self._vertex_count = int(len(self._vertices) / 8)
    
    def _process(self, delta_time: float) -> None:
        super()._process(delta_time)

        self._shader.update(self)
        self._texture.update()
        self._model.update()

        GL.glUseProgram(0)

    def destroy(self) -> None:
        self._model.destroy()
        self._texture.destroy()
        self._shader.destroy()