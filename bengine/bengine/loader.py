import os
import numpy as np
from PIL import Image
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

        # preload


    @staticmethod
    def load_shader(vertex_file: str, fragment_file: str) -> shaders.ShaderProgram:
        vertex_code = open(Loader.get_resource(f"shaders/{vertex_file}"), "r")
        fragment_code = open(Loader.get_resource(f"shaders/{fragment_file}"), "r")
        shader: int = shaders.compileProgram(
            shaders.compileShader(vertex_code, GL.GL_VERTEX_SHADER),
            shaders.compileShader(fragment_code, GL.GL_FRAGMENT_SHADER),
        )
        vertex_code.close()
        fragment_code.close()
        
        return shader

    @staticmethod
    def load_texture(texture_file: str) -> Image.Image:
        texture = Image.open(Loader.get_resource(f"textures/{texture_file}"))
        texture = texture.transpose(Image.FLIP_TOP_BOTTOM)
        return texture

    @staticmethod
    def get_resource(resource_path: str) -> str:
        for path in Loader._resource_paths:
            abs_path = Loader.get_abs_path(f"{path}{resource_path}")

            if os.path.exists(abs_path):
                return abs_path

        raise Exception(f"Failed to get resource at '{resource_path}'")

    @staticmethod
    def get_abs_path(path: str) -> str:        
        return os.path.join(os.path.abspath("."), path)

    @staticmethod
    def cleanup() -> None: pass

    @staticmethod
    def load_obj(model_path: str) -> np.ndarray:
        v = []
        vt = []
        vn = []
        vertices = []
        
        with open(Loader.get_resource(model_path), "r") as f:
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
        print(f"Loaded '{model_path}'")
        return vertices