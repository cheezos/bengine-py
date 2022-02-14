import ctypes
import numpy as np
from OpenGL import GL
from bengine.entity import Entity
from bengine.loader import Loader
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

        self.set_model(model_path)

        # Vertex Array Object
        self._vao = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self._vao)
        
        # Vertex Buffer Object
        self._vbo = GL.glGenBuffers(1)
        GL.glBindBuffer(GL.GL_ARRAY_BUFFER, self._vbo)
        GL.glBufferData(GL.GL_ARRAY_BUFFER, self._vertices.nbytes, self._vertices, GL.GL_STATIC_DRAW)
        
        # Vertex Position Coordinates
        GL.glEnableVertexAttribArray(0)
        GL.glVertexAttribPointer(0, 3, GL.GL_FLOAT, GL.GL_FALSE, self._vertices.itemsize * 8, ctypes.c_void_p(0))

        # Vertex Texture Coordinates
        GL.glEnableVertexAttribArray(1)
        GL.glVertexAttribPointer(1, 2, GL.GL_FLOAT, GL.GL_FALSE, self._vertices.itemsize * 8, ctypes.c_void_p(12))
        
        # Vertex Normal Coordinates
        GL.glEnableVertexAttribArray(2)
        GL.glVertexAttribPointer(2, 3, GL.GL_FLOAT, GL.GL_FALSE, self._vertices.itemsize * 8, ctypes.c_void_p(20))

        # Texture
        self._texture: Texture = Texture("textures/base.png")
        
        # Shader
        self._shader: Shader = Shader(UnlitShaderSource.vertex_shader, UnlitShaderSource.fragment_shader)        

    def set_model(self, model_path: str) -> None:
        self._vertices = OBJLoader.load(model_path)
        self._vertex_count = int(len(self._vertices) / 8)
    
    def _process(self, delta_time: float) -> None:
        super()._process(delta_time)

        self._shader.update()
        self._texture.update()
        GL.glBindVertexArray(self._vao)
        GL.glDrawElements(GL.GL_TRIANGLES, self._vertex_count, GL.GL_UNSIGNED_INT, 0)
    
    def cleanup(self) -> None:
        GL.glDeleteVertexArrays(1, self._vao)
        GL.glDeleteBuffers(1, self._vbo)