import os
from PIL import Image
from bengine.resources.shaders.unlit_shader import UnlitShaderSource
from OpenGL import GL
from OpenGL.GL import shaders

class Loader(object):
    @staticmethod
    def load_shader(vertex_code: str, fragment_code: str) -> shaders.ShaderProgram:
        shader: int = shaders.compileProgram(
            shaders.compileShader(vertex_code, GL.GL_VERTEX_SHADER),
            shaders.compileShader(fragment_code, GL.GL_FRAGMENT_SHADER),
        )
        
        return shader

    @staticmethod
    def load_texture(resource_path: str) -> Image.Image:
        texture = Image.open(Loader.get_resource(resource_path))
        texture = texture.transpose(Image.FLIP_TOP_BOTTOM)
        return texture

    @staticmethod
    def get_resource(resource_path: str) -> str:
        return Loader.get_abs_path(f"bengine/bengine/resources/{resource_path}")

    @staticmethod
    def get_abs_path(path: str) -> str:        
        return os.path.join(os.path.abspath("."), path)

    @staticmethod
    def cleanup() -> None: pass