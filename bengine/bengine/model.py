import ctypes
from bengine.loader import Loader
from OpenGL import GL

class Model:
    def __init__(self, model_path: str) -> None:
        self._vertices = Loader.load_obj(model_path)
        self._vertex_count = int(len(self._vertices) / 8)
        
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

    def destroy(self) -> None:
        GL.glDeleteVertexArrays(1, (self._vao,))
        GL.glDeleteBuffers(1, (self._vbo,))

    def _update(self) -> None:
        GL.glBindVertexArray(self._vao)
        GL.glEnableVertexArrayAttrib(self._vao, 0)
        GL.glEnableVertexArrayAttrib(self._vao, 1)
        GL.glEnableVertexArrayAttrib(self._vao, 2)
        GL.glDrawArrays(GL.GL_TRIANGLES, 0, self._vertex_count)
        GL.glDisableVertexArrayAttrib(self._vao, 0)
        GL.glDisableVertexArrayAttrib(self._vao, 1)
        GL.glDisableVertexArrayAttrib(self._vao, 2)
        GL.glBindVertexArray(0)