import os
from PIL import Image
from bengine.resources.shaders.unlit_shader import UnlitShaderSource
from OpenGL import GL
from OpenGL.GL import shaders

class Loader(object):
    _shaders: list[shaders.ShaderProgram] = []
    _textures: list[int] = []

    @staticmethod
    def load_shader(vertex_code: str, fragment_code: str) -> shaders.ShaderProgram:
        shader = shaders.compileProgram(
            shaders.compileShader(vertex_code, GL.GL_VERTEX_SHADER),
            shaders.compileShader(fragment_code, GL.GL_FRAGMENT_SHADER),
        )
        
        Loader._shaders.append(shader)
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
    def cleanup() -> None:
        for shader in Loader._shaders:
            GL.glDeleteProgram(shader)

        Loader._shaders = []