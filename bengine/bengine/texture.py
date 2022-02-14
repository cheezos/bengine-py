from bengine.loader import Loader
from PIL import Image

class Texture:
    def __init__(self, texture_path: str) -> None:
        self._texture: Image.Image = Loader.load_texture(texture_path)
        self._data: bytes = self._texture.convert("RGBA").tobytes()
    
    @property
    def texture(self) -> Image.Image:
        return self._texture
    
    @property
    def data(self) -> bytes:
        return self._data
    
    @property
    def width(self) -> int:
        return self._texture.width
    
    @property
    def height(self) -> int:
        return self._texture.height