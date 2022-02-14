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

        # Texture
        self._texture: Texture = Texture("textures/base.png")
        self._textures = GL.glGenTextures(1)
        GL.glBindTexture(GL.GL_TEXTURE_2D, self._textures)
        GL.glTexImage2D(GL.GL_TEXTURE_2D, 0, GL.GL_RGBA, self._texture.width, self._texture.height, 0, GL.GL_RGBA, GL.GL_UNSIGNED_BYTE, self._texture.data)
        
        # Shader
        self._shader: Shader = Shader(UnlitShaderSource.vertex_shader, UnlitShaderSource.fragment_shader)
        GL.glUseProgram(self._shader.program)
        GL.glEnable(GL.GL_DEPTH_TEST)
        GL.glBlendFunc(GL.GL_SRC_ALPHA, GL.GL_ONE_MINUS_SRC_ALPHA)
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_S, GL.GL_REPEAT)
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_T, GL.GL_REPEAT)

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

    def set_model(self, model_path: str) -> None:
        self._vertices = OBJLoader.load(model_path)
        self._vertex_count = int(len(self._vertices) / 8)
    
    def process(self, delta_time: float) -> None:
        GL.glUseProgram(self._shader.program)
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MIN_FILTER, GL.GL_LINEAR)
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MAG_FILTER, GL.GL_LINEAR)
        # GL.glEnable(GL_BLEND) if self.transparent else GL.glDisable(GL_BLEND)
        GL.glBindVertexArray(self._vao)
        GL.glBindTexture(GL.GL_TEXTURE_2D, self._textures)
        GL.glDrawArrays(GL.GL_TRIANGLES, 0, self._vertex_count)