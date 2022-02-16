from bengine.loader import Loader
from OpenGL import GL

class Texture:
    def __init__(self, texture_file: str) -> None:
        self._texture: int = Loader.load_texture(texture_file)

    def _update(self) -> None:
        GL.glActiveTexture(GL.GL_TEXTURE0)
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MIN_FILTER, GL.GL_LINEAR)
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MAG_FILTER, GL.GL_LINEAR)
        GL.glBindTexture(GL.GL_TEXTURE_2D, self._texture)
    
    def destroy(self) -> None: pass