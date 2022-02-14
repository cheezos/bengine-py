from OpenGL.GL import shaders
from OpenGL import GL
from bengine.loader import Loader

class Shader:
    def __init__(self, vertex_code: str, fragment_code: str) -> None:
        self._program: shaders.ShaderProgram = Loader.load_shader(vertex_code, fragment_code)
        GL.glUseProgram(self._program)
        GL.glEnable(GL.GL_DEPTH_TEST)
        GL.glBlendFunc(GL.GL_SRC_ALPHA, GL.GL_ONE_MINUS_SRC_ALPHA)
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_S, GL.GL_REPEAT)
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_T, GL.GL_REPEAT)
        GL.glGetUniformLocation(self._program, "textureSample")
        GL.glGetUniformLocation(self._program, "transformMatrix")
        GL.glGetUniformLocation(self._program, "projectionMatrix")
        GL.glGetUniformLocation(self._program, "viewMatrix")

    def update(self) -> None:
        GL.glUseProgram(self._program)
        