import ctypes
from bengine.loader import Loader
from OpenGL import GL

class Model:
    def __init__(self, model_path: str) -> None:
        #                           vao  vbo  vertices
        self._vertex_objects: tuple[int, int, int] = Loader.load_model(model_path)
        
    def destroy(self) -> None: pass
    
    def _update(self) -> None:
        GL.glBindVertexArray(self._vertex_objects[0])
        # GL.glEnableVertexArrayAttrib(self._vertex_objects[0], 0)
        # GL.glEnableVertexArrayAttrib(self._vertex_objects[0], 1)
        # GL.glEnableVertexArrayAttrib(self._vertex_objects[0], 2)
        GL.glDrawArrays(GL.GL_TRIANGLES, 0, self._vertex_objects[2])
        # GL.glDrawElements(GL.GL_TRIANGLES, int(self._vertex_objects[2] / 8), GL.GL_UNSIGNED_INT, 0)
        # GL.glDisableVertexArrayAttrib(self._vertex_objects[0], 0)
        # GL.glDisableVertexArrayAttrib(self._vertex_objects[0], 1)
        # GL.glDisableVertexArrayAttrib(self._vertex_objects[0], 2)
        GL.glBindVertexArray(0)