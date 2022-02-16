import ctypes
import os
import numpy as np
from OpenGL import GL
from OpenGL.GL import shaders
from PIL import Image

class Loader(object):
    _resource_paths: list[str] = [
        "bengine/bengine/resources/"
    ]

    _shaders: dict[str, int] = {}
    _textures: dict[str, int] = {}
    _vertices: dict[str, np.ndarray] = {}
    _vertex_objects: dict[str, tuple[int, int, int]] = {}

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

        Loader._preload_everything()

    @staticmethod
    def get_resource(resource_path: str) -> str:
        abs_path = ""
        
        for path in Loader._resource_paths:
            abs_path = Loader.get_abs_path(f"{path}{resource_path}")

            if os.path.exists(abs_path):
                return abs_path

        raise Exception(f"Failed to get resource at '{abs_path}'")

    @staticmethod
    def get_abs_path(path: str) -> str:        
        return os.path.join(os.path.abspath("."), path)

    @staticmethod
    def cleanup() -> None:
        for shader in Loader._shaders.values():
            GL.glDeleteProgram(shader)
        
        for texture in Loader._textures.values():
            GL.glDeleteTextures(1, (texture,))
        
        for vertex_objects in Loader._vertex_objects.values():
            GL.glDeleteVertexArrays(1, (vertex_objects[0],))
            GL.glDeleteBuffers(1, (vertex_objects[1],))

        print("Cleaned up resources")

    @staticmethod
    def load_shader(shader_folder: str) -> int:
        if shader_folder in Loader._shaders.keys():
            print(f"Using existing shader '{shader_folder}'")
            return Loader._shaders[shader_folder]
        else:
            vertex_code = open(Loader.get_resource(f"shaders/{shader_folder}/vertex.glsl"), "r")
            fragment_code = open(Loader.get_resource(f"shaders/{shader_folder}/fragment.glsl"), "r")
            shader: int = shaders.compileProgram(
                shaders.compileShader(vertex_code, GL.GL_VERTEX_SHADER),
                shaders.compileShader(fragment_code, GL.GL_FRAGMENT_SHADER),
            )
            vertex_code.close()
            fragment_code.close()
            Loader._shaders[shader_folder] = shader
            print(f"Loaded shader '{shader_folder}'")
            return shader

    @staticmethod
    def load_texture(texture_file: str) -> int:
        if texture_file in Loader._textures.keys():
            print(f"Using existing texture '{texture_file}'")
            return Loader._textures[texture_file]
        else:
            image = Image.open(Loader.get_resource(f"textures/{texture_file}"))
            image = image.transpose(Image.FLIP_TOP_BOTTOM)
            data: bytes = image.convert("RGBA").tobytes()
            texture = GL.glGenTextures(1)
            GL.glBindTexture(GL.GL_TEXTURE_2D, texture)
            GL.glTexImage2D(GL.GL_TEXTURE_2D, 0, GL.GL_RGBA, image.width, image.height, 0, GL.GL_RGBA, GL.GL_UNSIGNED_BYTE, data)
            Loader._textures[texture_file] = texture
            print(f"Loaded texture '{texture_file}'")
            return texture
        
    @staticmethod
    def load_model(model_path: str) -> tuple[int, int, int]:
        if model_path in Loader._vertex_objects.keys():
            print(f"Using existing model '{model_path}'")
            return Loader._vertex_objects[model_path]
        else:
            vertices = Loader._load_obj(model_path)
            vertex_count = int(len(vertices) / 8)
            vao = GL.glGenVertexArrays(1)
            GL.glBindVertexArray(vao)
            vbo = GL.glGenBuffers(1)
            GL.glBindBuffer(GL.GL_ARRAY_BUFFER, vbo)
            GL.glBufferData(GL.GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL.GL_STATIC_DRAW)
            GL.glEnableVertexAttribArray(0)
            GL.glVertexAttribPointer(0, 3, GL.GL_FLOAT, GL.GL_FALSE, vertices.itemsize * 8, ctypes.c_void_p(0))
            GL.glEnableVertexAttribArray(1)
            GL.glVertexAttribPointer(1, 2, GL.GL_FLOAT, GL.GL_FALSE, vertices.itemsize * 8, ctypes.c_void_p(12))
            GL.glEnableVertexAttribArray(2)
            GL.glVertexAttribPointer(2, 3, GL.GL_FLOAT, GL.GL_FALSE, vertices.itemsize * 8, ctypes.c_void_p(20))
            vo = (vao, vbo, vertex_count)
            Loader._vertex_objects[model_path] = vo
            print(f"Loaded model '{model_path}'")
            return vo

    @staticmethod
    def _load_obj(model_path: str) -> np.ndarray:
        if model_path in Loader._vertices.keys():
            print(f"Using existing OBJ '{model_path}'")
            return Loader._vertices[model_path]
        else:
            v = []
            vt = []
            vn = []
            vertices = []
            
            with open(Loader.get_resource(f"models/{model_path}"), "r") as f:
                line = f.readline()
                
                while line:
                    first_space = line.find(" ")
                    flag = line[0:first_space]
                    
                    if flag == "mtllib":
                        # ignore the material flag
                        pass
                    elif flag == "v":
                        # vertex
                        line = line.replace("v ", "")
                        line = line.split(" ")
                        l = [float(x) for x in line]
                        v.append(l)
                    elif flag == "vt":
                        line = line.replace("vt ", "")
                        line = line.split(" ")
                        l = [float(x) for x in line]
                        vt.append(l)
                    elif flag == "vn":
                        line = line.replace("vn ", "")
                        line = line.split(" ")
                        l = [float(x) for x in line]
                        vn.append(l)
                    elif flag == "f":
                        line = line.replace("f ", "")
                        line = line.replace("\n", "")
                        line = line.split(" ")
                        verts = []
                        texts = []
                        norms = []
                        
                        for _v in line:
                            l = _v.split("/")
                            position = int(l[0]) - 1
                            verts.append(v[position])
                            texture = int(l[1]) - 1
                            texts.append(vt[texture])
                            normal = int(l[2]) - 1
                            norms.append(vn[normal])
                        
                        tri_in_face = len(line) - 2
                        vertex_order = []
                        
                        for _i in range(tri_in_face):
                            vertex_order.append(0)
                            vertex_order.append(_i + 1)
                            vertex_order.append(_i + 2)
                        
                        for _i in vertex_order:
                            for _x in verts[_i]:
                                vertices.append(_x)
                            
                            for _x in texts[_i]:
                                vertices.append(_x)
                            
                            for _x in norms[_i]:
                                vertices.append(_x)
                    
                    line = f.readline()
            
            vertices = np.array(vertices, dtype=np.float32)
            f.close()
            Loader._vertices[model_path] = vertices
            print(f"Loaded obj '{model_path}'")
            return vertices

    @staticmethod
    def _preload_everything() -> None:
        print("\nPreloading resources...\n")
        
        for resource_path in Loader._resource_paths:
            shaders_path = f"{resource_path}shaders/"
            print(f"Preloading shaders from '{shaders_path}'")
            shaders = os.listdir(shaders_path)

            for shader in shaders:
                if shader != "__pycache__":
                    Loader.load_shader(shader)
            
            textures_path = f"{resource_path}textures/"
            print(f"Preloading textures from '{textures_path}'")
            textures = os.listdir(textures_path)

            for texture in textures:
                if texture.endswith(".png"):
                    Loader.load_texture(texture)

            models_path = f"{resource_path}models/"
            print(f"Preloading models from '{models_path}'")
            models = os.listdir(models_path)

            for model in models:
                if model.endswith(".obj"):
                    Loader.load_model(model)

        print("\nPreload complete\n")