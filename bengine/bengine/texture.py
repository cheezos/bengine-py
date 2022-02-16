from bengine.loader import Loader
from PIL import Image
from OpenGL import GL

class Texture:
    def __init__(self, texture_file: str) -> None:
        self._texture: Image.Image = Loader.load_texture(texture_file)
        self._data: bytes = self._texture.convert("RGBA").tobytes()
        self._textures = GL.glGenTextures(1)
        GL.glBindTexture(GL.GL_TEXTURE_2D, self._textures)
        GL.glTexImage2D(GL.GL_TEXTURE_2D, 0, GL.GL_RGBA, self._texture.width, self._texture.height, 0, GL.GL_RGBA, GL.GL_UNSIGNED_BYTE, self._data)
    
    def destroy(self) -> None:
        GL.glDeleteTextures(1, (self._textures,))

    def _update(self) -> None:
        GL.glActiveTexture(GL.GL_TEXTURE0)
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MIN_FILTER, GL.GL_LINEAR)
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MAG_FILTER, GL.GL_LINEAR)
        GL.glBindTexture(GL.GL_TEXTURE_2D, self._textures)