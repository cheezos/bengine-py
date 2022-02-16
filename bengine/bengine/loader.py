import os
from PIL import Image
from bengine.resources.shaders.unlit_shader import UnlitShaderSource
from OpenGL import GL
from OpenGL.GL import shaders

class Loader(object):
    _resource_paths: list[str] = [
        "bengine/bengine/resources/"
    ]

    @staticmethod
    def init(game_root_directory: str) -> None:
        res_path = f"{game_root_directory}/resources/"
        models_path = f"{res_path}models"
        shaders_path = f"{res_path}shaders"
        textures_path = f"{res_path}textures"

        if not os.path.exists(res_path):
            os.mkdir(res_path)
            print(f"Created resources directory at '{res_path}'")
        
        if not os.path.exists(models_path):
            os.mkdir(models_path)
            print(f"Created models directory at '{models_path}'")

        if not os.path.exists(shaders_path):
            os.mkdir(shaders_path)
            print(f"Created shaders directory at '{shaders_path}'")

        if not os.path.exists(textures_path):
            os.mkdir(textures_path)
            print(f"Created textures directory at '{textures_path}'")

        Loader._resource_paths.append(res_path)
        print(f"Added '{res_path}' to Loader paths")


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
        for path in Loader._resource_paths:
            abs_path = Loader.get_abs_path(f"{path}{resource_path}")

            if os.path.exists(abs_path):
                return abs_path

        raise Exception("Failed to get resource, file does not exist")

    @staticmethod
    def get_abs_path(path: str) -> str:        
        return os.path.join(os.path.abspath("."), path)

    @staticmethod
    def cleanup() -> None: pass